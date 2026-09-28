import json
from datetime import datetime

ALERT_FILE = r"E:\sentinel-ai\backend\app\data\alerts.json"

def save_alert(threat):

    alert = {
        "timestamp": str(datetime.now()),
        "threat": threat
    }

    try:
        with open(ALERT_FILE, "r") as f:
            alerts = json.load(f)
    except:
        alerts = []

    alerts.append(alert)

    with open(ALERT_FILE, "w") as f:
        json.dump(alerts, f, indent=4)
    
    print(f"[alert_service] 💾 Saved alert: {threat} | Total alerts: {len(alerts)}", flush=True)

def get_alerts():

    try:
        with open(ALERT_FILE, "r") as f:
            alerts = json.load(f)
            print(f"[alert_service] 📖 Retrieved {len(alerts)} alerts from {ALERT_FILE}", flush=True)
            return alerts
    except Exception as e:
        print(f"[alert_service] ❌ Failed to read alerts: {e}", flush=True)
        return []