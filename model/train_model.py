import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load data
df = pd.read_csv("data/customer_churn.csv")

print("Initial shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nMissing values before cleaning:\n", df.isna().sum())

# Drop CustomerID if it exists
if "CustomerID" in df.columns:
    df = df.drop("CustomerID", axis=1)

# Strip column names
df.columns = df.columns.str.strip()

# Clean string columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype(str).str.strip()

# Make sure target exists
if "Churn" not in df.columns:
    raise ValueError("Target column 'Churn' not found in dataset.")

# Encode ALL categorical feature columns except target
label_encoders = {}

categorical_cols = X_object_cols = [col for col in df.select_dtypes(include="object").columns if col != "Churn"]

print("\nCategorical columns to encode:", categorical_cols)

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Convert target to numeric
df["Churn"] = pd.to_numeric(df["Churn"], errors="coerce")

# Drop rows with missing target
df = df.dropna(subset=["Churn"])

# Fill any missing numeric feature values with median
for col in df.columns:
    if col != "Churn":
        df[col] = df[col].fillna(df[col].median())

print("\nMissing values after cleaning:\n", df.isna().sum())
print("\nChurn value counts:\n", df["Churn"].value_counts(dropna=False))
print("\nFinal shape:", df.shape)

# Features and target
X = df.drop("Churn", axis=1)
y = df["Churn"].astype(int)

# Final safety checks
if len(df) == 0:
    raise ValueError("Dataset became empty after cleaning.")

if X.isna().sum().sum() > 0:
    raise ValueError("There are still NaN values in X.")

if y.isna().sum() > 0:
    raise ValueError("There are still NaN values in y.")

print("\nFeature dtypes:\n", X.dtypes)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model
with open("model/churn_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save encoders
with open("model/encoders.pkl", "wb") as f:
    pickle.dump(label_encoders, f)

import matplotlib.pyplot as plt

feature_importance = pd.Series(model.feature_importances_, index=X.columns)
feature_importance = feature_importance.sort_values(ascending=False)

print("\nFeature Importance:\n", feature_importance)

feature_importance.plot(kind="barh", figsize=(8, 6))
plt.title("Feature Importance")
plt.xlabel("Importance Score")
plt.tight_layout()
plt.show()

print("\n✅ Model and encoders saved successfully!")