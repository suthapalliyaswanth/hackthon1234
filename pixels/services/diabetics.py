import numpy as np
from sklearn.ensemble import RandomForestClassifier

def train_model():
    # Dummy training data (you'd replace this with your real training data)
    X_train = np.array([
        [120, 20, 25, 120, 80],  # Sample 1
        [140, 30, 30, 130, 85],  # Sample 2
        [160, 40, 35, 140, 90],  # Sample 3
        # Add more training data as needed
    ])
    y_train = np.array([0, 1, 1])  # Dummy labels (0: No diabetes, 1: Diabetes)

    # Initialize and train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    return model

def predict_diabetes(model, user_input):
    # Make prediction using the trained model
    prediction = model.predict(user_input.reshape(1, -1))
    return prediction[0]

def interpret_prediction(prediction):
    if prediction == 0:
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

def get_user_input():
    # Prompt the user to input glucose, insulin, BMI, blood pressure - systolic, and blood pressure - diastolic values
    glucose = float(input("Enter Glucose level (mg/dL): "))
    insulin = float(input("Enter Insulin level (mIU/L): "))
    bmi = float(input("Enter BMI (kg/m^2): "))
    blood_pressure_systolic = float(input("Enter Blood Pressure - Systolic (mmHg): "))
    blood_pressure_diastolic = float(input("Enter Blood Pressure - Diastolic (mmHg): "))

    # Return user input as a numpy array
    return np.array([glucose, insulin, bmi, blood_pressure_systolic, blood_pressure_diastolic])

def main(glucose, insulin, bmi, blood_pressure_systolic, blood_pressure_diastolic):
    # Train the model
    trained_model = train_model()

    # Get user input
    user_input = np.array([glucose, insulin, bmi, blood_pressure_systolic, blood_pressure_diastolic])

    # Make prediction based on user input
    prediction = predict_diabetes(trained_model, user_input)

    # Interpret prediction and print result
    result, suggestions = interpret_prediction(prediction)
    print(f"Based on the provided information, the prediction is: {result}")
    if suggestions:
        print("\nSuggestions for managing diabetes:")
        for suggestion in suggestions:
            print(suggestion)

if __name__ == "__main__":
    main()