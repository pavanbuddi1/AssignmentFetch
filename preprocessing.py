import pandas as pd
import json
import uuid
import DataQualitySolutions

#In first step, the main focus is on checking whether the json data is valid.
def is_valid_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        return True
    except json.JSONDecodeError:
        return False
#Loading receipts.json to check if it is a valid json file.
file_path = 'receipts.json'
if is_valid_json_file(file_path):
    print("The JSON file is valid.")
else:
    print("Not valid JSON file. Fixing..\n")
    #fixing the json to address Data Quality issue.
    DataQualitySolutions.fix_json(file_path)
    print("File fixed. It is now valid JSON.\n")

#In the second step, I am checking if UUID in the receipts is in format and replacing if its not in the correct format.
#checking if id is in correct format
def is_valid_uuid(value):
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False

def check_uuid_format(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        for obj in data:
            if '_id' in obj:
                if is_valid_uuid(obj['_id']['$oid']):
                    print(f"Valid UUID format: {obj['_id']['$oid']}")
                else:
                    print(f"Invalid UUID format: {obj['_id']['$oid']}")
                    DataQualitySolutions.fix_uuid_format(obj)
                    print(f"Corrected UUID is: {obj['_id']['$oid']}")

    # Writing the corrected JSON data back to the file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

print("STATUS OF receipts.json file::::::\n")
check_uuid_format('receipts.json')

#In the 3rd step, I am checking if there are any missing values in columns of the data.
# Load data
receipts_df = pd.read_json('receipts.json')
# Check for missing values in receipts.json
missing_values_r = receipts_df.isnull().sum()
print("\n")
print("Missing values in Receipt files:\n", missing_values_r)
print("\n")
print("*****************************************\n")
#Handline the missing values by replacing with default value.
receipts_df.fillna('default_value', inplace=True)
updated_missing_values_r = receipts_df.isnull().sum()
print("\n")
print("Updated json values in Receipt files:\n", updated_missing_values_r)
print("\n")
