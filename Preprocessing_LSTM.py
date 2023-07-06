import pandas as pd
import numpy as np
from keras.utils import to_categorical
from sklearn.preprocessing import MinMaxScaler

# Load data from JSON file
df = pd.read_json('C:\\Users\\is0482sf\\Desktop\\Data_Listener\\User1\\log_1.json')

# Convert "type" to categorical
df['type'] = df['type'].astype('category')

# Fill NaN with 0
df = df.fillna(0)

# Create additional features
df['scaled_duration'] = MinMaxScaler().fit_transform(df['duration'].values.reshape(-1, 1))
df['scaled_distance'] = MinMaxScaler().fit_transform(df['distance'].values.reshape(-1, 1))
df['scaled_velocity'] = MinMaxScaler().fit_transform(df['velocity'].values.reshape(-1, 1))

# Segment data into 8-second sequences
X = []
y = []
sequence = []
start_time = df.iloc[0]['timestamp']
for i in range(len(df)):
    row = df.iloc[i]
    if row['timestamp'] - start_time > 8:
        if len(sequence) > 0:
            X.append(sequence)
            y.append(df.iloc[i - 1]['UserId'])
        start_time = row['timestamp']
        sequence = []
    sequence.append(row[['scaled_duration', 'scaled_distance', 'scaled_velocity']].values)
if len(sequence) > 0:
    X.append(sequence)
    y.append(df.iloc[-1]['UserId'])

# Convert to 3D array
X = np.array([np.array(seq) for seq in X])
y = to_categorical(y)