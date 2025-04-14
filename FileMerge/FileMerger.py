# -----------------------------------------
# FileMerger
# Author: Lauren Ryman
# Date: 4/11/2025
# Description: This program reads the first n lines from two user-specified input files and writes the
# values side-by-side into a new output file, one pair per line. It handles missing files, short files,
# and notifies the user of any mismatch in data length.
# -----------------------------------------
import os
import string
import pyinputplus as pyip

# --- DEV NOTE: ---
# File extensions are CASE-SENSITIVE on most systems (especially macOS/Linux).
# Please instruct users to type exact filenames, including correct case, when inputting source file names.
# The output file will be saved using the name provided by the user. A .txt extension is assumed or applied,
# but the user does NOT need to type '.txt' manually. the program will handle it or accept with/without.


# --- Welcome Message ---
print("\nWelcome to the File Line Merger Program.")
print("This program reads the first 'n' non-empty lines from two input files and writes them side-by-side to a new output file.")
print("Both files must contain at least 'n' valid (non-blank) lines.")

# --- Helper: Get platform-specific root directories ---
def get_search_paths():
    """Return a list of root directories to search based on the OS."""
    if os.name == 'nt':
        return [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]
    else:
        return ['/']

# --- Helper: Search recursively for a file ---
def find_file(filename, search_paths):
    """Search recursively for 'filename' starting from base paths."""
    for base_path in search_paths:
        for root, dirs, files in os.walk(base_path, topdown=True):
            if filename in files:
                return os.path.join(root, filename)
    return None

# --- Function to read first n **non-blank** lines from a file ---
def read_valid_lines_from_file(filename, expected_lines):
    """Reads and returns first n non-empty, non-whitespace-only lines from a file."""
    lines = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                stripped = line.strip()
                if stripped:  # Ignore blank or whitespace-only lines
                    lines.append(stripped)
                if len(lines) == expected_lines:
                    break
    except FileNotFoundError:
        print(f"Error: File not found: '{filename}'")
        return None
    except Exception as e:
        print(f"Error reading '{filename}': {e}")
        return None

    if len(lines) == 0:
        print(f"Error: The file '{filename}' contains no valid data lines.")
        return None
    if len(lines) < expected_lines:
        print(f"Error: The file '{filename}' only has {len(lines)} valid line(s), but you requested {expected_lines}.")
        return None

    return lines

# --- Main Program ---
try:
    file1 = pyip.inputFilename(prompt="\nEnter the name of the first input file: ")
    file2 = pyip.inputFilename(prompt="Enter the name of the second input file: ")
    output_file = pyip.inputFilename(prompt="Enter the name of the output file to create: ", allowRegexes=[r".*"])
    n = pyip.inputInt(prompt="Enter the number of lines to read from each file: ", min=1)

    # Try to locate missing files using system search
    search_paths = get_search_paths()
    for i, fname in enumerate([file1, file2]):
        if not os.path.exists(fname):
            print(f"Searching for '{fname}' on the system...")
            found_path = find_file(fname, search_paths)
            if found_path:
                print(f"Found '{fname}' at: {found_path}")
                if i == 0:
                    file1 = found_path
                else:
                    file2 = found_path
            else:
                print(f"Could not locate '{fname}' on the system.")

    # Read and validate usable lines
    lines1 = read_valid_lines_from_file(file1, n)
    lines2 = read_valid_lines_from_file(file2, n)

    if lines1 is None or lines2 is None:
        print("\nAborting program due to file validation error.")
    else:
        # Write to output file
        try:
            with open(output_file, 'w') as out_file:
                for i in range(n):
                    out_file.write(f"{lines1[i]}\t{lines2[i]}\n")

            print(f"\nOutput successfully written to '{output_file}'. Preview:\n")
            with open(output_file, 'r') as preview:
                for line in preview:
                    print(line.strip())

        except Exception as e:
            print(f"Error writing to output file: {e}")

except KeyboardInterrupt:
    print("\nProgram interrupted by user.")