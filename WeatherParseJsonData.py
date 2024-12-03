##################################################################
# Libraries
##################################################################
import os
import json

##################################################################
# Load JSON data from a file
##################################################################
json_path = r"D:\Dhavali\Projects\Weather Forecast Data Engineer Project\Dataset"

jsonFiles = os.listdir(json_path)

# List of all file names
filtered_files = [f for f in jsonFiles if f.startswith("WeatherData_2024") and f.endswith(".json")]

##################################################################
# Function to display row-wise data for each state
##################################################################
def display_state_data(data):
    if isinstance(data, dict):
        for state, seasons in data.items():
            print(f"\nState: {state}")
            if isinstance(seasons, dict):
                for season, details in seasons.items():
                    print(f"  Season: {season}")
                    if isinstance(details, dict):
                        for key, value in details.items():
                            print(f"    {key}: {value}")
                    else:
                        print(f"    {details}")
            else:
                print(f"  {seasons}")
                
##################################################################
# Process each file
##################################################################
for file in filtered_files:
    full_path = os.path.join(json_path, file)  # Concatenate path and file name
    print(f"\nReading file: {file}")

    with open(full_path, "r") as f:  # Use full_path to open the file
        data = json.load(f)

    # Display row-wise data for each state
    display_state_data(data)
