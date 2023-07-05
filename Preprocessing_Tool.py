import pandas as pd
import json

def process_data(data):
    df = pd.DataFrame(data)
    move_df = df[df['type'] == 'move'].sort_values('timestamp')

    # Calculate speed in x and y direction
    move_df['x_speed'] = move_df['x'].diff() / move_df['timestamp'].diff()
    move_df['y_speed'] = move_df['y'].diff() / move_df['timestamp'].diff()

    # Calculate the jerk which is the rate of change of acceleration
    move_df['jerk'] = move_df['acceleration'].diff() / move_df['timestamp'].diff()

    # Calculate the angle of movement
    move_df['angle'] = np.arctan2(move_df['y'].diff(), move_df['x'].diff())

    # Calculate curvature
    move_df['curve'] = move_df['angle'].diff() / move_df['distance']

    # Calculate the total elapsed time
    move_df['elapsed_time'] = move_df['timestamp'].max() - move_df['timestamp'].min()

    # Calculate sum of angles
    move_df['sum_of_angles'] = move_df['angle'].sum()

    # Get starting timestamp of acceleration
    move_df['accTimeatBeg'] = move_df.loc[move_df['acceleration'].first_valid_index(), 'timestamp']

    # Calculate trajectory length
    move_df['traj_length'] = move_df['distance'].sum()

    # Calculate means, std, min, max of the relevant columns
    statistics = ['mean', 'std', 'min', 'max']
    columns = ['x_speed', 'y_speed', 'velocity', 'acceleration', 'jerk', 'angle', 'curve']
    stats_df = move_df[columns].agg(statistics)

    # Flatten MultiIndex and convert to a dictionary
    stats_dict = stats_df.to_dict()

    # Add additional stats
    stats_dict['elapsed_time'] = move_df['elapsed_time'].iloc[-1]  # get the last value
    stats_dict['sum_of_angles'] = move_df['sum_of_angles'].iloc[-1]  # get the last value
    stats_dict['accTimeatBeg'] = move_df['accTimeatBeg'].iloc[0]  # get the first value
    stats_dict['traj_length'] = move_df['traj_length'].iloc[-1]  # get the last value

    return stats_dict


# Load the data
with open("C:\\Users\\is0482sf\\Desktop\\Data_Listener\\log_4.json") as f:
    data = json.load(f)

# Convert the data to a DataFrame
df = pd.DataFrame(data['data'])

# Separate the data by event type
df_move = df[df['type'] == 'move'].copy()

# Preprocess the 'move' data
df_move_processed = process_data(df_move)

print(df_move_processed)