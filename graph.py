import matplotlib.pyplot as plt
import pandas as pd

# Load the data from CSV file
file_path = 'meeting_location.csv'  #modify according to your file path
data = pd.read_csv(file_path)

# Extract longitude and latitude from the csv
longitude = data['longitude']
latitude = data['latitude']

# Plot the points
fig, ax = plt.subplots()
ax.scatter(latitude, longitude, color='black', s=20)

# Function to capture the click event and print coordinates
def onclick(event):
    if event.inaxes is not None:
        print(f"Latitude: {event.xdata:.6f}, Longitude: {event.ydata:.6f}")

cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Display the plot
plt.title('Geographical Plot of Longitude and Latitude (Black Points)')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()
