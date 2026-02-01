import csv
import sqlite3

# ========= CONFIG =========
CSV_FILE = "/opt/splunk/etc/system/lookups/ai_risk_scores.csv"
DB_FILE = "grc_risk.db"
# ==========================

# Connect to SQLite DB
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS risk_decisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    host TEXT,
    failed_logins INTEGER,
    privileged_logins INTEGER,
    risk_score INTEGER,
    severity TEXT,
    evaluated_time TEXT,
    auth_control_status TEXT,
    privilege_control_status TEXT
)
""")

# Read CSV and ingest
with open(CSV_FILE, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        failed_logins = int(row.get("failed_logins", 0))
        privileged_logins = int(row.get("privileged_logins", 0))
        risk_score = int(row.get("risk_score", 0))
        severity = row.get("severity")
        evaluated_time = row.get("evaluated_time")
        host = row.get("host")

        # ===== Authentication Control Logic =====
        if failed_logins >= 3:
            auth_control_status = "FAIL"
        else:
            auth_control_status = "PASS"

        # ===== Privileged Access Control Logic =====
        if privileged_logins > 0:
            privilege_control_status = "REVIEW"
        else:
            privilege_control_status = "PASS"

        # Insert into DB
        cursor.execute("""
        INSERT INTO risk_decisions (
            host,
            failed_logins,
            privileged_logins,
            risk_score,
            severity,
            evaluated_time,
            auth_control_status,
            privilege_control_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            host,
            failed_logins,
            privileged_logins,
            risk_score,
            severity,
            evaluated_time,
            auth_control_status,
            privilege_control_status
        ))

# Commit & close
conn.commit()
conn.close()

print("✔ Risk decisions ingested successfully into database.")
