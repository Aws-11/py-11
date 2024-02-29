# Import the json module to work with JSON data
import json

# Open the JSON file in read mode ('r')
with open('dataJSON.json') as fileJson:
    # Load the JSON data from the file into a Python dictionary
    readableJson = json.load(fileJson)

# Print the entire JSON data (loaded as a Python dictionary)
print(readableJson)

# Extract a specific value from the JSON data and assign it to a variable
variableOne = readableJson["name"]

# Print the extracted value
print(variableOne)
