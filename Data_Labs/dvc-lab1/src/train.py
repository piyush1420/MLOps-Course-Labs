import json

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 1. Load whichever version of the data DVC currently has
df = pd.read_csv("data/titanic.csv")

# 2. Pick the columns the model learns from, and drop rows with missing values
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]
df = df[features + ["Survived"]].dropna().copy()

# 3. Turn text into numbers: male -> 0, female -> 1
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

X = df[features]
y = df["Survived"]

# 4. Hold back 20% of passengers to test the model on
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Train the model and measure how often it's right
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
accuracy = accuracy_score(y_test, model.predict(X_test))

# 6. Save the results so DVC can track and compare them
metrics = {
    "accuracy": round(float(accuracy), 4),
    "rows_used": len(df),
    "train_rows": len(X_train),
    "test_rows": len(X_test),
}
with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print(metrics)
