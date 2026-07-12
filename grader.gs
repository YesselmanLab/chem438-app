/**
 * grader.gs — the CHEM 438 grading backend (Google Apps Script).
 *
 * Deploy this bound to a Google Sheet (see README). It:
 *   • holds the hidden answer keys (in a "Keys" sheet), never sent to the browser
 *   • grades a submission server-side and writes one row per (student, lesson)
 *     into the "Gradebook" sheet
 *   • accepts key uploads from build.py via an admin token
 *
 * Set one Script Property first:  ADMIN_TOKEN = <a long random string>
 * (Project Settings → Script properties). build.py uses the same token.
 *
 * The compare() function below MUST match authoring/norm.py::compare.
 */

function doPost(e) {
  var body;
  try { body = JSON.parse(e.postData.contents); }
  catch (err) { return json({ ok: false, error: "bad json" }); }

  if (body.action === "set_keys") return setKeys(body);
  return gradeSubmission(body);         // default action
}

function doGet() { return json({ ok: true, service: "chem438-grader" }); }

// ---------------- grading ----------------
function gradeSubmission(sub) {
  if (!sub || !sub.lesson || !sub.rosterId) return json({ ok: false, error: "missing fields" });
  var keys = loadKeys(sub.lesson);
  if (!keys) return json({ ok: false, error: "no keys for " + sub.lesson });

  var results = {};
  (sub.answers || []).forEach(function (a) {
    var k = keys[a.id];
    if (!k) return;                                   // written / unknown: skip
    if (k.kind === "mcq") {
      results[a.id] = (a.choice === k.answer);
    } else if (k.kind === "code_var") {
      results[a.id] = (!a.error && a.outputs && compare(k.expected, a.outputs[0], k.tol || 1e-6));
    } else if (k.kind === "code_fn") {
      results[a.id] = (!a.error && a.outputs && compare(k.expected, a.outputs, k.tol || 1e-6));
    }
  });

  writeRow(sub, results);
  return json({ ok: true, results: results });
}

function compare(e, a, tol) {                          // mirror of norm.py::compare
  if (Array.isArray(e)) {
    return Array.isArray(a) && e.length === a.length &&
      e.every(function (x, i) { return compare(x, a[i], tol); });
  }
  if (typeof e === "boolean" || typeof a === "boolean") return e === a;
  if (typeof e === "number" && typeof a === "number") {
    return Math.abs(e - a) <= tol + tol * Math.max(Math.abs(e), Math.abs(a));
  }
  return e === a;
}

// ---------------- gradebook (upsert one row per student+lesson) ----------------
function writeRow(sub, results) {
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);                                // serialize read-modify-write
  try {
    var sh = sheet("Gradebook");
    ensureHeader(sh, sub);
    var data = sh.getDataRange().getValues();
    var rowIdx = -1;
    for (var r = 1; r < data.length; r++) {
      if (data[r][2] === sub.rosterId && data[r][3] === sub.lesson) { rowIdx = r + 1; break; }
    }
    var auto = 0, got = 0;
    for (var qid in results) { auto++; if (results[qid]) got++; }
    var row = [new Date(), sub.name, sub.rosterId, sub.lesson, got, auto,
               JSON.stringify(results), JSON.stringify(rawByQid(sub))];
    if (rowIdx === -1) sh.appendRow(row);
    else sh.getRange(rowIdx, 1, 1, row.length).setValues([row]);
  } finally { lock.releaseLock(); }
}

function ensureHeader(sh, sub) {
  if (sh.getLastRow() > 0) return;
  sh.appendRow(["timestamp", "name", "rosterId", "lesson", "score", "outOf", "results", "raw"]);
}

function rawByQid(sub) {                                // keep raw answers for auditing
  var o = {};
  (sub.answers || []).forEach(function (a) {
    o[a.id] = a.kind === "mcq" ? a.choice : (a.kind === "written" ? a.text : (a.error || a.outputs));
  });
  return o;
}

// ---------------- keys storage ("Keys" sheet: col A lesson, col B json) ----------------
function loadKeys(lesson) {
  var sh = sheet("Keys");
  var data = sh.getDataRange().getValues();
  for (var r = 0; r < data.length; r++) {
    if (data[r][0] === lesson) { try { return JSON.parse(data[r][1]).keys; } catch (e) { return null; } }
  }
  return null;
}

function setKeys(body) {                                // called by build.py
  var token = PropertiesService.getScriptProperties().getProperty("ADMIN_TOKEN");
  if (!token || body.token !== token) return json({ ok: false, error: "unauthorized" });
  var sh = sheet("Keys");
  var data = sh.getDataRange().getValues();
  var blob = JSON.stringify({ keys: body.keys });
  for (var r = 0; r < data.length; r++) {
    if (data[r][0] === body.lesson) { sh.getRange(r + 1, 2).setValue(blob); return json({ ok: true, updated: body.lesson }); }
  }
  sh.appendRow([body.lesson, blob]);
  return json({ ok: true, added: body.lesson });
}

// ---------------- helpers ----------------
function sheet(name) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  return ss.getSheetByName(name) || ss.insertSheet(name);
}
function json(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
