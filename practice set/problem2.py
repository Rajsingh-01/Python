# problem 2 
# ques= write a python program to print the contains on a directry using the os module 
# search online for the fuction which does that
import os

# Ask the user to enter the path of the directory
directory_path = "C:\\Users\\Raj_10\\Downloads"

try:
    # Get a list of all files and folders in the specified directory
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: The directory does not exist.")
except NotADirectoryError:
    print("Error: The path is not a directory.")
except PermissionError:
    print("Error: Permission denied to access this directory.")
