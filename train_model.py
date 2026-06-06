import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

df = pd.read_csv("threat_dataset.csv")
print("Dataset shape: ",df.shape)
person_encoder = LabelEncoder()
time_encoder = LabelEncoder()
threat_encoder = LabelEncoder()

df["person"] = person_encoder.fit_transform(
    df["person"]
)

df["time"] = time_encoder.fit_transform(
    df["time"]
)

df["threat"] = threat_encoder.fit_transform(
    df["threat"]
)

X = df.drop("threat", axis=1)

y = df["threat"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("Accuracy:", accuracy)

joblib.dump(
    model,
    "threat_model.pkl"
)

joblib.dump(
    person_encoder,
    "person_encoder.pkl"
)

joblib.dump(
    time_encoder,
    "time_encoder.pkl"
)

joblib.dump(
    threat_encoder,
    "threat_encoder.pkl"
)

print("Model Saved")