import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np

# 1. Load Data (In a real setup, this comes from a Splunk Export)
# For your demo, we will create a 'Feature Matrix' from your logs
data = {
    'host': ['DESKTOP-01', 'DESKTOP-01', 'DESKTOP-01'],
    'failed_logins': [4, 1, 20],  # 20 is a huge anomaly!
    'privileged_logins': [1, 0, 5]
}
df = pd.DataFrame(data)

# 2. Initialize the Isolation Forest
# contamination=0.1 means we expect 10% of logs to be 'weird'
model = IsolationForest(contamination=0.1, random_state=42)

# 3. Train & Predict
# The AI looks at the 'patterns' of logins
df['anomaly_signal'] = model.fit_predict(df[['failed_logins', 'privileged_logins']])

# 4. Convert AI signal to GRC Risk Score (0-100)
# -1 from Isolation Forest means 'Anomaly'
df['risk_score'] = df['anomaly_signal'].apply(lambda x: 90 if x == -1 else 10)
df['severity'] = df['risk_score'].apply(lambda x: 'HIGH' if x > 70 else 'LOW')
df['evaluated_time'] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')

# 5. Save to the CSV file your Ingestion script needs
df.to_csv("/opt/splunk/etc/system/lookups/ai_risk_scores.csv", index=False)
print("✔ AI Model (Isolation Forest) has identified anomalies and updated CSV.")
