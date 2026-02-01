🛡️ Automated SOC-to-GRC Risk Assessment using Splunk & AI
📌 Project Overview

This project implements an automated SOC-to-GRC pipeline that converts raw Windows security events into governance-ready risk decisions. Using Splunk for log analytics and a backend AI-based decision engine, the system evaluates authentication and privileged access controls and exposes results through an interactive dashboard and REST APIs.

Unlike traditional SOC dashboards that focus only on alerts, this project demonstrates how SIEM data can directly support Governance, Risk, and Compliance (GRC) functions.

🎯 Problem Statement

Security teams receive thousands of authentication events daily, but:

GRC teams need control effectiveness, not raw logs

Manual audit evidence collection is slow and error-prone

Risk severity decisions depend heavily on human judgment

This project bridges that gap by automatically mapping SOC alerts to GRC controls and generating explainable AI-driven risk decisions.

🧠 Key Concepts Implemented

SOC → GRC integration

Explainable AI (rule-based decision intelligence)

Control-level risk evaluation

Automated compliance evidence generation

Backend-driven dashboards (no heavy frontend frameworks)

🏗️ Architecture
Windows Security Logs
        ↓
Splunk (SIEM)
        ↓
Control Evaluation (SPL)
        ↓
AI Risk Scoring (Weighted Logic)
        ↓
CSV Lookup Output
        ↓
Python Backend Ingestion
        ↓
SQLite Database
        ↓
Flask REST APIs & Dashboard

🔍 Log Sources Used
Event ID	Description
4624	Successful login
4625	Failed login
4672	Privileged logon
4634	Logoff
🧩 GRC Controls Implemented
🔐 Authentication Control

Evaluates failed login behavior

Status: PASS / FAIL

👑 Privileged Access Control

Evaluates privileged logins

Status: PASS / REVIEW

🤖 AI Risk Logic (Explainable)

The system uses weighted risk scoring, not black-box ML:

Factor	Weight
Failed logins	High
Privileged logins	Medium

Severity is inferred as:

LOW

MEDIUM

HIGH

This approach ensures auditability and transparency, which is critical in GRC environments.

📊 Dashboard Features

Interactive control-wise view

Authentication vs Privileged Access separation

AI risk score & severity

Dynamic updates based on login behavior

Backend-rendered UI using Flask

🔗 REST API Endpoints
Endpoint	Description
/	Health check
/api/risk/latest	Latest AI risk decision
/api/risk/high	High / Critical risks
/dashboard	Interactive GRC dashboard
🛠️ Tech Stack

SIEM: Splunk

Backend: Python, Flask

Database: SQLite

OS Logs: Windows Security Events

AI Logic: Rule-based explainable intelligence

▶️ How to Run
# Activate environment
source venv/bin/activate

# Ingest latest AI risk scores
python3 ingest_risk_scores.py

# Start backend
python3 app.py


Access dashboard:

http://<KALI_IP>:5000/dashboard

🎬 How to Demo

Show raw login logs in Splunk

Show control evaluation SPL query

Show AI risk score output

Refresh dashboard to show updated risk

Explain how controls map to governance decisions

📈 Future Enhancements

ML-based anomaly detection

Time-series risk trend analysis

ISO 27001 / NIST CSF control mapping

Auto-refresh dashboard

Integration with ticketing systems

🧠 Key Takeaway

This project demonstrates how SIEM data can be transformed into continuous GRC intelligence, enabling faster and more informed risk decisions.

👨‍💻 Author

Karthik Nallamamidi
Cybersecurity | SOC | GRC | SIEM