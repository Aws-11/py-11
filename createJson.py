import json

# Navigation text for options
navText = """
1: Wipe Data
2: Create Data
3: Exit
"""

# Function to get user input for key-value pair
def getInput():
    key = input("Enter key: ")
    value = input("Enter value: ")
    return key, value

# Function to wipe the JSON file
def wipeData():
    confirmation = input("Are you sure you want to wipe the JSON file? (yes/no): ")
    if confirmation.lower() in ("yes","y"):
        with open('data.json', 'w') as file:
            file.write("")
        print("JSON file wiped successfully.")
    else:
        print("Wipe operation aborted.")

# Function to create or update data in the JSON file
def createData():
    try:
        while True:
            key, value = getInput()

            # Read existing JSON data or initialize as empty dictionary
            try:
                with open('data.json', 'r') as file:
                    existingData = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                existingData = {}

            # Update data with new input
            existingData[key] = value

            # Write updated data back to the file
            with open('data.json', 'w') as file:
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

# Function to handle navigation options
def navOption():
    while True:
        print(navText)
        userInput = str(input("Option: "))
        match userInput:
            case "1":
                wipeData()
            case "2":
                createData()
            case "3":
                print("Shutting down...")
                exit()
            case _ :
                continue

# Start the navigation
navOption()
