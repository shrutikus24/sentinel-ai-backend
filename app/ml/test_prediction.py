import pandas as pd
import joblib
model = joblib.load(
    r"E:\sentinel-ai\backend\app\ml\threat_detector.pkl"
)

df = pd.read_csv(
    r"E:\cicids2017_cleaned.csv"
)

# Take first row
sample = df.iloc[0]

actual = sample["Attack Type"]

features = sample.drop("Attack Type")

prediction = model.predict([features])[0]

label_map = {
    0: "Normal Traffic",
    1: "DDoS",
    2: "Port Scanning"
}

print("Actual:", actual)
print("Predicted:", label_map[prediction])