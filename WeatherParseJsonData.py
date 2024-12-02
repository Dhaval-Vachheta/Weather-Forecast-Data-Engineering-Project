##################################################################
# Libraries
##################################################################
import pandas as pd
import json
import time

##################################################################
# Load JSON data from a file
##################################################################
json_path = "D:\Dhavali\Projects\Weather Forecast Data Engineer Project\Dataset"
with open(json_path+"\WeatherData_2024-11-30_23_15_49.json","r") as file:
    data = json.load(file)

# Display JSON Data
# print(data)

##################################################################
# Convert the JSON data to a pandas dataframe
##################################################################
df = pd.DataFrame.from_dict(data, orient='index')

# Display Data
# print(df)

##################################################################
# Function for displaying the state wise data
##################################################################
def state_wise_data_generation(df):
    for index, row in df.iterrows():
        print(f"State: {index}")
        print(f"    Winter: {row['Winter']}")
        print(f"    Summer: {row['Summer']}")
        print(f"    Monsoon: {row['Monsoon']}")
        print("-" * 20)
        time.sleep(1) # Pause for a second to show 1 by 1 data

# Calling state_wise_data_generation Function
state_wise_data_generation(df)