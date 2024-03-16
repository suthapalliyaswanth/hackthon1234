import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor

def train_model(data):
    # Separate features and target variable
    X = data.drop(columns=['Sleep Quality'])
    y = data['Sleep Quality']

    # Separate numeric and categorical columns
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    # Define preprocessing steps for numeric and categorical data
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Create a pipeline with preprocessing and model
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('regressor', RandomForestRegressor())])

    # Train the model
    pipeline.fit(X, y)
    
    return pipeline

def predict_sleep_quality(model, input_data):
    # Predict sleep quality
    y_pred = model.predict(input_data)
    return y_pred

data = pd.read_csv('newwwxxxx.csv')
model = train_model(data)
def main(start, end, regularity, steps, movements_per_hour,time_in_bed_seconds, time_asleep_seconds,
                                                                time_before_sleep_seconds, window_start,
                                                                window_stop, snore_time):
    # Load the dataset

    # Train the model

    # Accept user input values
    input_values = {
        'Start': start,
        'End': end,
        'Regularity': regularity,
        'Steps': steps,
        'Movements per hour': movements_per_hour,
        'Time in bed (seconds)': time_in_bed_seconds,
        'Time asleep (seconds)': time_asleep_seconds,
        'Time before sleep (seconds)': time_before_sleep_seconds,
        'Window start': window_start,
        'Window stop': window_stop,
        'Snore time': snore_time
    }

    # Create a DataFrame from user input
    input_data = pd.DataFrame([input_values])

    # Predict sleep quality based on user input
    return predict_sleep_quality(model, input_data)
    
