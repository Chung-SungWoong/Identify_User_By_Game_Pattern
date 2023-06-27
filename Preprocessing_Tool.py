import pandas as pd
import json
import numpy as np

def preprocess_movement_data(df):
    df = df.sort_values('timestamp')

    # calculate displacement
    df['dx'] = df['x'].diff()
    df['dy'] = df['y'].diff()

    # calculate distance
    df['distance'] = np.sqrt(df['dx']**2 + df['dy']**2)

    # calculate velocity
    df['dt'] = df['timestamp'].diff()
    df['velocity'] = df['distance'] / df['dt']

    # calculate acceleration
    df['acceleration'] = df['velocity'].diff() / df['dt']

    # Calculate elapsed time
    df['elapsed_time'] = df['timestamp'].max() - df['timestamp'].min()

    # Calculate total travelled distance
    df['total_distance'] = df['distance'].sum()

    # Calculate average velocity and standard deviation
    df['avg_velocity'] = df['velocity'].mean()
    df['std_velocity'] = df['velocity'].std()

    # Calculate average acceleration and standard deviation
    df['avg_acceleration'] = df['acceleration'].mean()
    df['std_acceleration'] = df['acceleration'].std()

    # End-to-end line
    df['end_to_end_line'] = np.sqrt((df['x'].iloc[-1] - df['x'].iloc[0])**2 + 
                                    (df['y'].iloc[-1] - df['y'].iloc[0])**2)

    # Efficiency
    df['efficiency'] = df['end_to_end_line'] / df['distance'].sum()

    return df

# Load the data
with open("C:\\Users\\is0482sf\\Desktop\\Data_Listener\\log_4.json") as f:
    data = json.load(f)

# Convert the data to a DataFrame
df = pd.DataFrame(data['data'])

# Separate the data by event type
df_move = df[df['type'] == 'move'].copy()
df_click = df[df['type'] == 'click'].copy()
df_press = df[df['type'] == 'press'].copy()

# Preprocess the 'move' data
df_move_processed = preprocess_movement_data(df_move)

print(df_move_processed)


# TODO: Preprocess the 'click' and 'press' data as necessary
# df_click_processed = preprocess_click_data(df_click)
# df_press_processed = preprocess_press_data(df_press)