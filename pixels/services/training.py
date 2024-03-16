import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

data = pd.read_csv('diabetes.csv', header=0)

X = data.drop('res', axis=1)
y = data['res']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

try:
    with open('logistic_regression_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)

    with open('logistic_regression_model.pkl', 'wb') as file:
        pickle.dump(model, file)

def predict(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    features = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

    # Convert the list to a numpy array and reshape it
    features_array = np.array(features).reshape(1, -1)

    # Make predictions using the model
    if model.predict(features_array) == 0:
        return "No diabetes", None
    else:
        suggestions = [
            "1. Monitor your blood sugar levels regularly.",
            "2. Follow a balanced diet with emphasis on whole grains, fruits, vegetables, and lean proteins.",
            "3. Engage in regular physical activity such as walking, swimming, or cycling for at least 30 minutes a day.",
            "4. Avoid sugary drinks and processed foods.",
            "5. Take prescribed medications as directed by your healthcare provider.",
            # Add more suggestions as needed
        ]
        return "Diabetes", suggestions 

# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy*100)
