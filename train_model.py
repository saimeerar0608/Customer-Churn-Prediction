import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_excel("Final Customer Churn predict dataset.xlsx")

# Remove customerID
df.drop("customerID", axis=1, inplace=True)

# Encode text columns
le = LabelEncoder()

columns_to_encode = [
    'gender',
    'Dependents',
    'PhoneService',
    'MultipleLines',
    'InternetService',
    'OnlineSecurity',
    'OnlineBackup',
    'Streaming TV',
    'Streaming Movies',
    'Contract',
    'PaymentMethod',
    'Churn'
]

for col in columns_to_encode:
    df[col] = le.fit_transform(df[col])

# Features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Logistic Regression
model = LogisticRegression(max_iter=5000)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save model
joblib.dump(model, "churn_model.pkl")

print("Model Trained Successfully")