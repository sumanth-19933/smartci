import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


DATA_FILE = "build_history.csv"
MODEL_FILE = "build_failure_model.pkl"


def train_model():
    data = pd.read_csv(DATA_FILE)

    features = [
        "changed_files",
        "previous_failures",
        "build_duration"
    ]

    X = data[features]
    y = data["failed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("Model Accuracy:", accuracy_score(y_test, predictions))
    print(classification_report(y_test, predictions))

    joblib.dump(model, MODEL_FILE)
    print("Model saved successfully.")


def predict_failure(changed_files, previous_failures, build_duration):
    model = joblib.load(MODEL_FILE)

    input_data = pd.DataFrame([{
        "changed_files": changed_files,
        "previous_failures": previous_failures,
        "build_duration": build_duration
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        print("Prediction: Build may FAIL")
    else:
        print("Prediction: Build may PASS")

    print(f"Failure probability: {probability:.2%}")


if __name__ == "__main__":
    train_model()