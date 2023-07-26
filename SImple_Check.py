# Import necessary libraries
import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load and preprocess data
def load_and_preprocess_data(filename):
    # Load the data
    with open(filename, "r") as file:
        combined_data = json.load(file)

    # Convert the data to a DataFrame for easier manipulation
    df = pd.json_normalize(combined_data['data'])

    # Initialize the MinMaxScaler and LabelEncoder
    scaler = MinMaxScaler()
    le = LabelEncoder()

    # Normalize the features
    features = ['x', 'y', 'distance', 'velocity', 'acceleration']
    df[features] = scaler.fit_transform(df[features])

    # Encode the target variable
    df['UserId'] = le.fit_transform(df['UserId'])

    return df, features

# Define LSTM model
def create_model(input_shape, output_shape):
    # Define the LSTM model
    model = Sequential()
    model.add(LSTM(100, activation='relu', input_shape=input_shape))
    model.add(Dense(output_shape, activation='softmax'))
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model

# Train the model
def train_model(model, df, features, segment_length):
    # Train the model with each segment
    for i in range(0, len(df) - segment_length):
        # Extract a segment of length segment_length starting at position i
        segment = df[features].values[i : i + segment_length].reshape(1, segment_length, len(features))

        # Get the most common label in this segment
        label = df['UserId'][i : i + segment_length].mode()[0]

        # Train the model with this segment
        model.fit(segment, np.array([label]), epochs=1, verbose=0)

# Main function to run the script
def main():
    df, features = load_and_preprocess_data("//Users//chung_sungwoong//Desktop//Practice//Identify_User_By_Game_Pattern//combined.json")
    model = create_model((None, len(features)), df['UserId'].nunique())
    train_model(model, df, features, 100)

if __name__ == "__main__":
    main()
