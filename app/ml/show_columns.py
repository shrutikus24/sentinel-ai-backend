import pandas as pd

df = pd.read_csv(
    r"E:\cicids2017_cleaned.csv",
    nrows=1
)

print(df.columns.tolist())