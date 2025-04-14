Author: Lauren Ryman
Date: 3/8/2025

Overview
FileFunction2 is a Python script that demonstrates an advanced way to find a specific file (numbers.txt) anywhere on your local system. It then reads integer values from that file, calculates their total and average, and outputs the results. Key features include:

Recursive file search using Python’s os.walk

Error handling with messages for missing files, empty files, or invalid integers

Automatic change of the current working directory to the folder containing numbers.txt once it’s found

How It Works
Initial Check

The script checks if numbers.txt exists in the current working directory.

If found, it checks if the file is non-empty.

System-Wide Search

If numbers.txt is not in the current directory, the script searches drive C:\ (or another specified path) by walking all subdirectories.

Every directory visited is printed to help you see the search in progress.

Once found, it changes the working directory to where numbers.txt resides.

Reading and Processing the File

Each line of numbers.txt is read and split into tokens.

Tokens that can be converted to integers are summed.

The average is then computed and displayed.

Non-integer tokens generate a warning message and are skipped.

Requirements
Python 3.x (the script uses standard libraries: os, sys)

Windows OS (the path C:\ is hard-coded; adapt for other operating systems if needed)

Usage
Place your numbers.txt file in the same folder as this script or somewhere else on C:\.

Open a Terminal / Command Prompt and navigate to the folder containing FileFunction2.py.

Run the script:

bash
Copy code
python FileFunction2.py
Observe the search process. If the script doesn’t find numbers.txt in the current directory, it will search throughout C:\.

Output is either:

“Total: <sum>” and “Average: <average>” if valid integers were found, or

An appropriate error message if the file is missing/empty.

Demonstration
If numbers.txt is in a different folder, the script will display messages like:

mathematica
Copy code
Searching directory: C:\Some\Folder
Did NOT find numbers.txt in C:\Some\Folder.
...
Found numbers.txt in C:\Some\Folder\Nested
Found file at: C:\Some\Folder\Nested\numbers.txt
Working directory changed to: C:\Some\Folder\Nested
Total: 45
Average: 9.0
Notes & Tips
Change start_directory: In the script, the variable start_directory is set to "C:\\". If you want to search a different drive or directory, you can change this value.

Non-integer values: The script prints a message like Skipping invalid integer: x for any non-numeric data in numbers.txt.

Permission / Access Errors: If the script encounters a directory it cannot access, it prints a warning and continues.

License
This script is provided for educational and portfolio purposes. You are free to use, modify, and distribute it as you see fit, but please give credit to the original author if you share significant modifications.

Contact
Questions?
Feel free to open an issue or send a message via GitHub.

