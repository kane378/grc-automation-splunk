from flask import Flask, jsonify, render_template_string
import sqlite3

app = Flask(__name__)

DB_FILE = "grc_risk.db"


# ---------- DB CONNECTION ----------
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


# ---------- HOME ----------
@app.route("/")
def home():
    return "GRC AI Risk API is running"


# ---------- API: LATEST RISK ----------
@app.route("/api/risk/latest")
def latest_risk():
    conn = get_db_connection()
    row = conn.execute(
        "SELECT * FROM risk_decisions ORDER BY evaluated_time DESC LIMIT 1"
    ).fetchone()
    conn.close()

    if row:
        return jsonify(dict(row))
    return jsonify({"message": "No data available"})


# ---------- API: HIGH / CRITICAL ----------
@app.route("/api/risk/high")
def high_risk():
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT * FROM risk_decisions WHERE severity IN ('HIGH','CRITICAL')"
    ).fetchall()
    conn.close()

    return jsonify([dict(r) for r in rows])


# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT * FROM risk_decisions ORDER BY evaluated_time DESC"
    ).fetchall()
    conn.close()

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI GRC Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
            }
            h2 {
                margin-left: 20px;
            }
            .controls {
                margin-left: 20px;
            }
            button {
                padding: 10px 15px;
                margin: 5px;
                border: none;
                border-radius: 4px;
                background: #007bff;
                color: white;
                cursor: pointer;
            }
            button:hover {
                background: #0056b3;
            }
            .card {
                background: white;
                border-radius: 6px;
                padding: 15px;
                margin: 15px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            }
            .PASS { color: green; font-weight: bold; }
            .FAIL { color: red; font-weight: bold; }
            .REVIEW { color: orange; font-weight: bold; }
        </style>

        <script>
            function toggle(id) {
                let el = document.getElementById(id);
                el.style.display = (el.style.display === "none") ? "block" : "none";
            }
        </script>
    </head>

    <body>
        <h2>AI-driven GRC Dashboard</h2>

        <div class="controls">
            <button onclick="toggle('auth')">Authentication Control</button>
            <button onclick="toggle('priv')">Privileged Access Control</button>
            <button onclick="toggle('ai')">AI Risk Decision</button>
        </div>

        <!-- AUTH CONTROL -->
        <div id="auth" class="card" style="display:none;">
            <h3>Authentication Control</h3>
            {% for r in rows %}
                <p>
                    <b>{{ r['host'] }}</b> |
                    Failed Logins: {{ r['failed_logins'] }} |
                    Status:
                    <span class="{{ r['auth_control_status'] }}">
                        {{ r['auth_control_status'] }}
                    </span>
                </p>
            {% endfor %}
        </div>

        <!-- PRIVILEGED CONTROL -->
        <div id="priv" class="card" style="display:none;">
            <h3>Privileged Access Control</h3>
            {% for r in rows %}
                <p>
                    <b>{{ r['host'] }}</b> |
                    Privileged Logins: {{ r['privileged_logins'] }} |
                    Status:
                    <span class="{{ r['privilege_control_status'] }}">
                        {{ r['privilege_control_status'] }}
                    </span>
                </p>
            {% endfor %}
        </div>

        <!-- AI DECISION -->
        <div id="ai" class="card" style="display:none;">
            <h3>AI Risk Assessment</h3>
            {% for r in rows %}
                <p>
                    <b>{{ r['host'] }}</b> |
                    Risk Score: {{ r['risk_score'] }} |
                    Severity: <b>{{ r['severity'] }}</b> |
                    Time: {{ r['evaluated_time'] }}
                </p>
            {% endfor %}
        </div>

    </body>
    </html>
    """

    return render_template_string(html, rows=rows)


# ---------- RUN ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
