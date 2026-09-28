import pandas as pd

file_path = file_path = r"E:\cicids2017_cleaned.csv"
print("Loading dataset...")

df = pd.read_csv(file_path)

print("\nAll Columns:")
print(df.columns.tolist())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
for col in df.columns:
    print(col)

print("\nLast Column:")
print(df.columns[-1])

print("\nSample Rows:")
print(df.head())

# Try to find label column automatically
possible_labels = ["Label", "label", "Attack", "Attack Type", "Class"]

for col in possible_labels:
    if col in df.columns:
        print(f"\nLabel Distribution ({col}):")
        print(df[col].value_counts())

        print("\nData Types:\n")
        print(df.dtypes)
        break