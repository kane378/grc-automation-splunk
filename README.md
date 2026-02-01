# 🛡️ AI-Assisted Automated GRC Control Monitoring using Splunk

---

## 📌 Project Overview

This project implements an **automated SOC-to-GRC pipeline** that converts raw Windows security events into **governance-ready risk decisions**.

Using **Splunk** for log analytics and a **Python-based AI decision engine**, the system evaluates authentication and privileged access controls, calculates risk severity, detects anomalous login behavior using machine learning, and presents results through an interactive dashboard.

Unlike traditional SOC dashboards that focus only on alerts, this project demonstrates how **SIEM data can directly support Governance, Risk, and Compliance (GRC) functions**.

---

## 🎯 Problem Statement

Security teams generate thousands of authentication events daily, but:

- GRC teams need **control effectiveness**, not raw logs  
- Manual audit evidence collection is **slow and error-prone**  
- Risk severity decisions depend heavily on **human judgment**

This project bridges that gap by automatically mapping SOC telemetry to GRC controls and generating **explainable, AI-assisted risk decisions**.

---

## 🧠 Key Concepts Implemented

- SOC → GRC integration  
- Explainable AI (rule-based decision intelligence)  
- Machine learning–based anomaly detection  
- Control-level risk evaluation  
- Automated compliance evidence generation  
- Backend-driven dashboards using Flask  

---

## 🏗️ Architecture

Windows Security Logs
↓
Splunk (SIEM)
↓
Control Evaluation (SPL)
↓
AI Risk & Anomaly Analysis
↓
CSV Lookup Output
↓
Python Backend Ingestion
↓
SQLite GRC Database
↓
Flask Dashboard


---

## 🔍 Log Sources Used

| Event ID | Description |
|--------|------------|
| 4624 | Successful login |
| 4625 | Failed login |
| 4672 | Privileged logon |
| 4634 | Logoff |

---

## 🧩 GRC Controls Implemented

### 🔐 Authentication Control
- Evaluates failed login behavior  
- Status: **PASS / FAIL**

### 👑 Privileged Access Control
- Evaluates privileged logins  
- Status: **PASS / REVIEW**

---

## 🤖 AI Component

### Explainable AI (Rule-Based)

The system uses **weighted risk scoring** to infer severity:

| Factor | Weight |
|------|-------|
| Failed logins | High |
| Privileged logins | Medium |

Severity levels:
- **LOW**
- **MEDIUM**
- **HIGH**

This ensures **auditability and transparency**, which is critical in GRC environments.

---

### AI Feature Engineering

Raw Windows security events are transformed into behavioral features suitable for machine learning:

- Number of failed login attempts  
- Number of privileged logins  
- Time-of-day of authentication activity  

---

### Machine Learning Model

An **Isolation Forest** algorithm is used for anomaly detection.

- Unsupervised learning (no labels required)  
- Learns normal authentication behavior  
- Flags deviations as anomalous  

---

### AI and GRC Integration

AI outputs are **not treated as alerts**.  
Instead, anomaly results are correlated with GRC controls to **support governance decisions**.

This enables:
- Faster risk prioritization  
- Reduced manual log review  
- Continuous GRC intelligence  

---

### AI Outputs

| Output | Description |
|------|------------|
| Anomaly Flag | NORMAL / ANOMALOUS |
| Anomaly Score | Degree of abnormality |
| Risk Score | Rule-based risk calculation |
| Severity | LOW / MEDIUM / HIGH |

All AI outputs are persisted in the GRC database for **audit and historical analysis**.

---

## 📊 Dashboard Features

- Control-wise risk visualization  
- Authentication vs Privileged Access separation  
- AI anomaly status and severity  
- Dynamic updates based on login behavior  
- Backend-rendered UI using Flask  

---

## 🛠️ Tech Stack

- **SIEM:** Splunk  
- **Backend:** Python, Flask  
- **Database:** SQLite  
- **Logs:** Windows Security Events  
- **AI:** Explainable logic + Isolation Forest  

---

## ▶️ How to Run

```bash
# Activate virtual environment
source venv/bin/activate

# Ingest latest AI risk scores
python3 ingest_risk_scores.py

# Start dashboard
python3 app.py
Access the dashboard:

http://<KALI_IP>:5000
🎬 How to Demo
Generate login activity on Windows

Show raw authentication logs in Splunk

Execute control evaluation SPL queries

Run AI risk ingestion

Refresh the dashboard

Explain governance-level decisions

📈 Future Enhancements
Advanced ML and ensemble anomaly detection

Time-series risk trend analysis

ISO 27001 / NIST CSF control mapping

Auto-refresh dashboard

Ticketing and workflow system integration

⚠️ Limitations
AI requires sufficient historical authentication data

Anomalies do not directly imply confirmed compromise

Thresholds and models require periodic tuning

🧠 Key Takeaway
This project demonstrates how SIEM data can be transformed into continuous, AI-assisted GRC intelligence, enabling faster, auditable, and governance-ready risk decisions.

👨‍💻 Author
Karthik Nallamamidi
Cybersecurity | SOC | GRC | SIEM