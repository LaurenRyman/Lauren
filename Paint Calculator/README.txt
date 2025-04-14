PaintCalc: Paint Job Estimator
Author: Lauren Ryman
Date: 4/11/2025

Overview
PaintCalc is a Python program that calculates the amount of paint and labor needed for a painting job, based on:

The total square feet of wall space.

The price per gallon of paint.

It then displays and prints a cost estimate in a neatly formatted table using the tabulate library. Users can optionally repeat estimates for multiple paint jobs, and each result is saved (appended) to a time-stamped output file.

Key Features
User-Friendly Input

Prompts for the square footage and paint price using pyinputplus for robust validation.

Automatically re-prompts if the user enters values below the specified minimum.

Paint & Labor Calculations

One gallon covers 122 sq ft (rounded up to the nearest gallon).

8 hours of labor per gallon of paint.

$47.00 per hour labor rate.

Neat, Aligned Output

Uses the tabulate library for a professional, grid-like layout.

Columns align properly on decimal points.

Output File

Generates a unique filename (e.g. paintestimate_YYYYMMDD_HHMMSS_Username.txt) using datetime and getpass.

Appends each estimate to this output file with the same grid formatting.

Displays the saved file’s full path.

Repeatable

Prompts “Would you like to estimate another paint job?” until the user chooses “no.”

Catches KeyboardInterrupt so the user can press Ctrl+C to exit gracefully.

Requirements
Python 3.x

pyinputplus for user input validation

nginx
Copy code
pip install pyinputplus
tabulate for table formatting

nginx
Copy code
pip install tabulate
Windows, macOS, or Linux (OS agnostic; though path defaults might differ slightly)

Usage
Install Dependencies:

bash
Copy code
pip install pyinputplus tabulate
Run the Script:

bash
Copy code
python PaintCalc.py
Enter Required Values:

Square feet of wall space (e.g. 800.0).

Price per gallon of paint (e.g. 25.99).

View the Estimate:

The program prints a grid table with gallons of paint, labor hours, paint cost, labor cost, and total.

Check the Output File:

A new file named paintestimate_<timestamp>_<username>.txt is created in the same directory.

The table is appended each time you run a new estimate.

Repeat or Quit:

Answer “yes” or “no” when asked if you want another estimate.

Press Ctrl+C to exit immediately if desired.

Example Output
swift
Copy code
Paint Job Estimate
+--------------------------------+----------+
| Item                           |  Amount  |
+--------------------------------+----------+
| Gallons of paint required      |       10 |
| Hours of labor required        |     80.0 |
| Cost of the paint              |  $ 259.90 |
| Labor charges                  |  $3760.00 |
| Total cost of the job          |  $4019.90 |
+--------------------------------+----------+

Estimate saved to: C:\Path\to\your\project\paintestimate_20250411_103501_Lauren.txt
License
Use, modify, or share this program for educational and portfolio purposes. Please credit the original author (Lauren Ryman) if you publish significant modifications.

Contact
Questions or ideas?
Open an issue on GitHub or send a message.

Enjoy your painting cost estimates!