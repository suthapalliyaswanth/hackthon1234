import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
# Load the dataset
url = "Heart_Disease_Prediction.csv"
heart_data = pd.read_csv(url)

# Convert non-numeric values in 'Age' column to NaN
heart_data['Age'] = pd.to_numeric(heart_data['Age'], errors='coerce')

# Handle missing values (imputation or removal)
heart_data.dropna(subset=['Age'], inplace=True)  # Remove rows with missing 'Age' values
# Alternatively, you can impute missing values
# heart_data['Age'].fillna(heart_data['Age'].mean(), inplace=True)

# Separate features and target variable
X = heart_data.drop('Heart Disease', axis=1)
y = heart_data['Heart Disease']

# Standardize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X, y)

def preprocess_input(features):
    # Preprocess input features using the same scaler used during training
    if scaler is not None:
        features = scaler.transform([features])
    return features

def predict_heart_disease(features):
    # Preprocess input features
    processed_features = preprocess_input(features)
    # Make predictions
    max_hr = features[7]
    print(max_hr)
    if model is not None:
        prediction = model.predict(processed_features)
        return prediction[0] if max_hr > 45 and max_hr < 129 else 'Presence'
    else:
        return None

def get_user_input():
    age = float(input("Enter Age: "))
    sex = float(input("Enter Sex (0 for female, 1 for male): "))
    chest_pain_type = float(input("Enter Chest Pain Type: "))
    blood_pressure = float(input("Enter Blood Pressure: "))
    cholesterol = float(input("Enter Cholesterol: "))
    fbs_over_120 = float(input("Enter Fasting Blood Sugar (FBS) over 120 (0 for No, 1 for Yes): "))
    ekg_results = float(input("Enter EKG Results: "))
    max_hr = float(input("Enter Maximum Heart Rate: "))
    exercise_angina = float(input("Enter Exercise-Induced Angina (0 for No, 1 for Yes): "))
    st_depression = float(input("Enter ST Depression: "))
    slope_of_st = float(input("Enter Slope of ST: "))
    num_vessels_fluro = float(input("Enter Number of Vessels Fluro: "))
    thallium = float(input("Enter Thallium: "))

    features = [age, sex, chest_pain_type, blood_pressure, cholesterol, fbs_over_120,
                ekg_results, max_hr, exercise_angina, st_depression, slope_of_st,
                num_vessels_fluro, thallium]
    return features

def main(age, sex, chest_pain_type, blood_pressure, cholesterol, fbs_over_120,
                ekg_results, max_hr, exercise_angina, st_depression, slope_of_st,
                num_vessels_fluro, thallium):
    # Get user input
    user_input = [age, sex, chest_pain_type, blood_pressure, cholesterol, fbs_over_120,
                ekg_results, max_hr, exercise_angina, st_depression, slope_of_st,
                num_vessels_fluro, thallium]
    
    
    # Predict heart disease
    prediction = predict_heart_disease(user_input)
    print(prediction)
    if prediction is not None:
        if prediction.startswith('P'):
            return "Heart disease is likely."
        else:
            return "Heart disease is not likely."
    else:
        return "Model is not available. Please train a model first."

if __name__ == "__main__":
    main()

