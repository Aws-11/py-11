import json

# Create a dictionary containing some sample data
dataJSON = {
    "name": "John Doe",
    "age": 51,
    "occupation": "Carpenter"
}

# Open the file named 'dataJSON.json' in write mode ('w')
# The 'with' statement ensures proper file handling and closure
with open('dataJSON.json', 'w') as file:
    # Write the contents of the dataJSON dictionary to the file in JSON format
    # 'indent=4' is used for pretty printing, adding indentation for readability
    json.dump(dataJSON, file, indent=4)
