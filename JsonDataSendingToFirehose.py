##################################################################
# Libraries
##################################################################
import os
import json
import boto3
from botocore.exceptions import ClientError

##################################################################
# Load AWS Credentials from Config File
##################################################################
CONFIG_FILE_PATH = "AWS_Config.json"  # Path to the configuration file

# Load credentials
with open(CONFIG_FILE_PATH, 'r') as config_file:
    aws_config = json.load(config_file)

# Extract credentials
AWS_ACCESS_KEY_ID = aws_config['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = aws_config['aws_secret_access_key']
AWS_REGION = aws_config['region_name']

# Initialize boto3 Firehose client with loaded credentials
firehose_client = boto3.client(
    'firehose',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

##################################################################
# AWS Firehose Configuration
##################################################################
FIREHOSE_STREAM_NAME = "your-firehose-stream-name"  # Replace with your Firehose stream name

##################################################################
# Json Data Reading and Processing
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
# Function to Send Records to AWS Firehose
##################################################################
def send_to_firehose(records, stream_name):
    for record in records:
        try:
            # Convert record to JSON string
            record_data = json.dumps(record)
            
            # Send record to Firehose
            response = firehose_client.put_record(
                DeliveryStreamName=stream_name,
                Record={'Data': record_data + "\n"}  # Add newline for text-based services
            )
            print(f"Record sent to Firehose: {response['RecordId']}")
        except ClientError as e:
            print(f"Error sending record to Firehose: {e}")

##################################################################
# Send All Records to Firehose
##################################################################
send_to_firehose(all_records, FIREHOSE_STREAM_NAME)
