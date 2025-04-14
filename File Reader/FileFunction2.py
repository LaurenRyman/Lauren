# -----------------------------------------
# FileFunction2
# Author: Lauren Ryman
# Date: 3/8/2025
# Description: More advanced version of FIleFunction that searches the system for the file location and changes
# the current working directory to the file location the numbers.txt file is found
# -----------------------------------------
import os
import sys

def find_file(filename, start_dir):
    """
    Recursively search for a file with the given filename starting at start_dir.
    Prints each directory it searches, indicating if the file was not found there.
    Returns the full path if found; otherwise, returns None.
    """

    def onerror(error):
        print(f"Error accessing {error.filename}: {error.strerror}")

    for dirpath, dirnames, files in os.walk(start_dir, onerror=onerror):
        # Print the directory we're searching
        print(f"Searching directory: {dirpath}")

        # Check if our target file is in this directory
        if filename in files:
            print(f"Found {filename} in {dirpath}")
            return os.path.join(dirpath, filename)
        else:
            # If not found in this directory, let the user know
            print(f"Did NOT find {filename} in {dirpath}.")
    return None

def check_file(filename):
    """
    Checks if the file exists and contains data.
    If not found in the current directory, searches the entire computer (starting at a specified root).
    When found, it sets the current working directory to the file's location.
    Returns True if the file exists and is not empty; otherwise, returns False.
    """

    # 1. Check if file exists in the current working directory.
    if os.path.exists(filename):
        print("Found file in current directory.")
        try:
            with open(filename, 'r') as file_obj:
                content = file_obj.read().strip()
        except Exception as e:
            print(f"Error reading file: {e}")
            return False

        if content:
            return True
        else:
            print("File is empty.")
            return False

    else:
        print("File not found in current directory. Searching entire computer...")
        # Adjust this path if you want to search another drive or directory
        start_directory = "C:\\"

        found_path = find_file(filename, start_directory)
        if found_path:
            print(f"Found file at: {found_path}")
            # Change current working directory to the file's directory.
            file_dir = os.path.dirname(found_path)
            try:
                os.chdir(file_dir)
                print("Working directory changed to:", os.getcwd())
            except Exception as e:
                print(f"Error changing directory: {e}")
                return False

            # Verify that the file isn't empty
            try:
                with open(filename, 'r') as file_obj:
                    content = file_obj.read().strip()
            except Exception as e:
                print(f"Error reading file: {e}")
                return False

            if content:
                return True
            else:
                print("File is empty after search.")
                return False
        else:
            print("File not found during search.")
            return False

# Main Program
filename = "numbers.txt"

if not check_file(filename):
    print("Either the file does not exist or it is empty!")
    sys.exit(1)
else:
    try:
        with open(filename, 'r') as file_obj:
            numbers_str = file_obj.read().split()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    total = 0
    count = 0
    for num_str in numbers_str:
        try:
            total += int(num_str)
            count += 1
        except ValueError:
            print(f"Skipping invalid integer: {num_str}")

    if count > 0:
        average = total / count
        print("Total:", total)
        print("Average:", average)
    else:
        print("No valid numbers found.")
