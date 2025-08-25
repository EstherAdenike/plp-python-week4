# Ask the user for a filename
file_name = input("Please Enter the file name: ")

# handle errors if it doesn’t exist or can’t be read.
try:
    with open(file_name, "r") as file:
        data = file.read()
        print (data)
except FileNotFoundError: 
    print("File not found. Please check the filename.")
except PermissionError:
    print("You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")