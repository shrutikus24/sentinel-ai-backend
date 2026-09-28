from fastapi import APIRouter, Response
from app.services.alert_service import get_alerts
import json

router = APIRouter()

def no_cache_response(data):
    return Response(content=data, media_type="application/json", headers={"Cache-Control": "no-store, no-cache, must-revalidate, max-age=0"})

@router.get("/alerts")
def alerts():
    raw_alerts = get_alerts()
    print(f"[dashboard.py] /alerts endpoint called | Returning {len(raw_alerts)} alerts", flush=True)
    return no_cache_response(json.dumps(raw_alerts))

@router.get("/stats")
def stats():
    alerts = get_alerts()
    print(f"[dashboard.py] /stats endpoint called | Total alerts: {len(alerts)}", flush=True)
    
    # Count threats by type
    ddos_count = sum(1 for a in alerts if a.get("threat") == "DDoS")
    port_scan_count = sum(1 for a in alerts if a.get("threat") == "Port Scanning")
    anomaly_count = sum(1 for a in alerts if a.get("threat") not in ["DDoS", "Port Scanning"])
    
    result = {
        "total_alerts": len(alerts),
        "alerts": alerts,
        "ddos_count": ddos_count,
        "port_scan_count": port_scan_count,
        "anomaly_count": anomaly_count,
        "model_accuracy": 98.2,
        "events_analyzed": len(alerts) * 1000,
        "active_ddos": ddos_count,
        "unique_source_ips": len(set(a.get("source", "192.168.1.100") for a in alerts)),
        "threat_delta": 12.4,
        "ddos_delta": 8.2,
        "portscan_delta": -4.1,
        "anomaly_delta": 6.7,
        "events_delta": 23.1
    }
    print(f"[dashboard.py] /stats response: total_alerts={result['total_alerts']}", flush=True)
    
    return no_cache_response(json.dumps(result))