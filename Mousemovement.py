import json
import matplotlib.pyplot as plt

# Read the JSON file
with open('/Users/chung_sungwoong/Desktop/Practice/Identify_User_By_Game_Pattern/log.json', 'r') as json_file:
    data = json.load(json_file)

# Extract x and y coordinates of mouse movement events
x_coords = []
y_coords = []

for event in data['events']:
    if event['type'] == 'move':
        x_coords.append(event['x'])
        y_coords.append(event['y'])

# Plot the x-y graph
plt.plot(x_coords, y_coords, linestyle='-', marker='o', markersize=2)
plt.xlabel('X-Coordinates')
plt.ylabel('Y-Coordinates')
plt.title('Mouse Movement')
plt.show()