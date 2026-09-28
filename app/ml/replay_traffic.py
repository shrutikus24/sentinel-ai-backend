import importlib
import time
import sys
import os

sys.path.append(r"E:\sentinel-ai\backend")

# Import dynamically so static analyzers do not require pandas in this environment.
pandas = importlib.import_module("pandas")
pd = pandas

# Import dynamically so static analyzers do not require joblib in this environment.
joblib = importlib.import_module("joblib")

from app.services.alert_service import save_alert

# Load model
model = joblib.load(
    r"E:\sentinel-ai\backend\app\ml\threat_detector.pkl"
)

# Load dataset
df = pd.read_csv(
    r"E:\cicids2017_cleaned.csv"
)

# Keep only classes used in training
df = df[df["Attack Type"].isin([
    "Normal Traffic",
    "DDoS",
    "Port Scanning"
])]

label_map = {
    0: "Normal Traffic",
    1: "DDoS",
    2: "Port Scanning"
}

print(f"[replay_traffic] Starting traffic replay on {len(df)} rows...", flush=True)

for index, row in df.iterrows():

    actual = row["Attack Type"]

    features = row.drop("Attack Type")

    features_df = pd.DataFrame([features])

    prediction = model.predict(features_df)[0]

    threat = label_map[prediction]

    if threat != "Normal Traffic":
        print(f"[replay_traffic] 🚨 ALERT | Threat: {threat} | Actual: {actual}", flush=True)
        try:
            save_alert(threat)
            print(f"[replay_traffic] ✅ Alert saved to alerts.json", flush=True)
        except Exception as e:
            print(f"[replay_traffic] ❌ Failed to save alert: {e}", flush=True)
    else:
        print(f"[replay_traffic] ✅ Normal Traffic | Actual: {actual}", flush=True)
    time.sleep(1)