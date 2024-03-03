import json

def getInput():
    key = input("Enter key: ")
    value = input("Enter value: ")
    return key, value

def createData():
    try:
        while True:
            key, value = getInput()

            # Read existing JSON data or initialize as empty dictionary
            try:
                with open('data2.json', 'r') as file:
                    existingData = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                existingData = {}

            # Update data with new input
            existingData[key] = value

            # Write updated data back to the file
            with open('data2.json', 'w') as file:
                json.dump(existingData, file, indent=4)
            print("JSON file updated successfully.")

            # Ask if user wants to continue adding data
            userInput = input("Do you want to stop (yes/no(Enter)): ")
            if userInput.lower() in ("yes", "y"):
                break

    except FileNotFoundError:
        print("Error: JSON file not found.")
    except PermissionError:
        print("Error: Permission denied to write to JSON file.")
    except OSError as e:
        print(f"Error: {e.strerror} - {e.filename}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def check_data():
    with open('data2.json') as file:
        data= json.load(file)
