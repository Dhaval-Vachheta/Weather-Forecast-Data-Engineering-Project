##################################################################
# Libraries
##################################################################
import os
import json

##################################################################
# Json Data Reading
##################################################################
# Path to the folder containing JSON files
json_path = r"D:\Dhavali\Projects\Weather Forecast Data Engineer Project\Dataset"

# Get the list of json files
json_files = os.listdir(json_path)

# Empty list for files name
files = [file for file in json_files]

# List to store all records row-wise
all_records = []

# Full path of json files
for file in files:
    full_path = os.path.join(json_path, file)
    print(f"Processing file: {full_path}")

    # Read the JSON file
    with open(full_path, 'r') as f:
        weather_data = json.load(f)

    ##################################################################
    # Getting row-wise (1 by 1) record of JSON file
    ##################################################################
    def json_row_wise_data(weatherData, fileName):
        row_records = []  # List to store records
        if isinstance(weatherData, dict):
            for state, seasons in weatherData.items():
                if isinstance(seasons, dict):
                    for season, details in seasons.items():
                        if isinstance(details, dict):
                            # Create a dictionary for each row
                            record = {
                                'FileName': fileName,
                                'State': state,
                                'Season': season,
                                **details  # Unpack the details dictionary
                            }
                            row_records.append(record)
                        else:
                            print(f"Unexpected format in state: {state}, season: {season}")
        
        return row_records

    # Append the records of this file to the main list
    all_records.extend(json_row_wise_data(weather_data, file))

##################################################################
# Final result of row wise data
##################################################################
# Display all records
for record in all_records:
    print(record)
