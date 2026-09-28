import joblib
import pandas as pd

model = joblib.load(
    "app/ml/threat_detector.pkl"
)

label_map = {
    0: "Normal Traffic",
    1: "DDoS",
    2: "Port Scanning"
}

EXPECTED_FEATURES = list(model.feature_names_in_)

def predict_threat(features: dict):
    # Ensure all expected features are present
    full_features = {feat: features.get(feat, 0) for feat in EXPECTED_FEATURES}
    
    df = pd.DataFrame([full_features])
    df = df[EXPECTED_FEATURES]  # Ensure correct column order

    prediction = model.predict(df)[0]

    confidence = max(
        model.predict_proba(df)[0]
    ) * 100

    return {
        "threat": label_map[prediction],
        "confidence": round(confidence, 2)
    }