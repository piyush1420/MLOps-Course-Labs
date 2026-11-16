import pandas as pd

# Load the current data (version 1, the raw file)
df = pd.read_csv("data/titanic.csv")
print("Missing values before cleaning:", int(df.isna().sum().sum()))

# 1. Fill missing ages with the median (middle) age
df["Age"] = df["Age"].fillna(df["Age"].median())

# 2. Fill the 2 missing ports with the most common port
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# 3. Drop the Cabin column, since most of its values are missing
df = df.drop(columns=["Cabin"], errors="ignore")

print("Missing values after cleaning:", int(df.isna().sum().sum()))

# Save over the same file: this becomes version 2
df.to_csv("data/titanic.csv", index=False)
