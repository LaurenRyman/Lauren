FileMerger
Author: Lauren Ryman
Date: 4/11/2025

Overview
FileMerger is a Python script that reads the first n non-empty lines from two user-specified input files and writes them side-by-side to a new output file. Along the way, it:

Handles missing or short files via error messages or by attempting a system-wide search (on Windows, macOS, or Linux).

Ignores blank lines (only counts lines that have non-whitespace text).

Reports partial or missing data if a file has fewer than n valid lines.

This makes it ideal for quickly merging tabular or line-based data from two sources in a user-friendly manner.

Key Features
User-Friendly Prompts
Uses pyinputplus to ask for:

The first input filename

The second input filename

The name of the output file

The number of lines to read from each input file

Automatic File Location

If a user-supplied file doesn’t exist in the current directory, the script attempts a recursive system search:

On Windows (os.name == 'nt'), it searches all detected drive letters (C:\\, D:\\, etc.).

On macOS or Linux, it starts from the root directory /.

Blank Line Filtering

Lines containing only whitespace are ignored.

Users need truly non-empty lines to satisfy the “read first n lines” requirement.

Side-by-Side Output

Each line from the first file is written next to the corresponding line from the second file (separated by a tab).

The output is appended with “.txt” if you like, or you can use any filename you wish.

Error & Exception Handling

Gracefully reports short files, missing files, or I/O errors.

Catches KeyboardInterrupt to handle Ctrl+C gracefully.

Requirements
Python 3.x

pyinputplus for user input:

nginx
Copy code
pip install pyinputplus
Tested on Windows, macOS, and Linux. (The system-wide file search logic differs slightly by OS.)

Usage
Install Requirements
If not already installed:

bash
Copy code
pip install pyinputplus
Run the Script

bash
Copy code
python FileMerger.py
Follow Prompts

Enter the two input filenames.

Enter the desired output filename.

Specify the number of lines (n) to read from each file.

Output Preview

After successfully merging, the program displays a preview of the merged lines.

Example Interaction
vbnet
Copy code
Welcome to the File Line Merger Program.
Enter the name of the first input file: firstone.txt
Enter the name of the second input file: secondone.txt
Enter the name of the output file to create: merged_result.txt
Enter the number of lines to read from each file: 5

Searching for 'firstone.txt' on the system...
Found 'firstone.txt' at: C:\Users\Lauren\Documents\firstone.txt

Searching for 'secondone.txt' on the system...
Could not locate 'secondone.txt' on the system.

Error: File not found: 'secondone.txt'
Aborting program due to file validation error.
Or, if both files are found and have enough lines:

python
Copy code
Output successfully written to 'merged_result.txt'. Preview:

123   abc
456   def
789   ghi
111   jkl
222   mno
Tips and Edge Cases
Case Sensitivity: On Windows, filenames are generally case-insensitive. On Linux/macOS, they can be case-sensitive.

File Extension: The program doesn’t force .txt on output_file, but you can provide any name (e.g., myOutput.csv).

Blank Lines: If an input file has blank or whitespace-only lines, they don’t count toward the first n lines. This can result in fewer “valid” lines than you expect.

License
Feel free to use and modify FileMerger for educational and portfolio purposes. If you share improvements, please acknowledge the original author (Lauren Ryman).

Contact
Questions or suggestions?
Open an issue on GitHub or send a message.