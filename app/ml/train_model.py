import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

print("Loading dataset...")

df = pd.read_csv(r"E:\cicids2017_cleaned.csv")

# Keep only major classes for MVP
classes = [
    "Normal Traffic",
    "DDoS",
    "Port Scanning"
]

df = df[df["Attack Type"].isin(classes)]

# Use only 200k records for faster training
df = df.sample(
    n=200000,
    random_state=42
)

print("\nClass Distribution:")
print(df["Attack Type"].value_counts())

# Encode labels
mapping = {
    "Normal Traffic": 0,
    "DDoS": 1,
    "Port Scanning": 2
}

df["label"] = df["Attack Type"].map(mapping)

# Features
X = df.drop(columns=["Attack Type", "label"])

# Replace missing values
X = X.fillna(0)

# Target
y = df["label"]

print("\nSplitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training model...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Evaluating...")

preds = model.predict(X_test)

print(classification_report(y_test, preds))

joblib.dump(model, "threat_detector.pkl")

print("\nModel saved successfully!")