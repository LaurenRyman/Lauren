# -----------------------------------------
# PaintCalc
# Author: Lauren Ryman
# Date: 4/11/2025
# Description: Estimates paint and labor costs and prints a professional table using tabulate.
# -----------------------------------------
import pyinputplus as pyip
import math
from tabulate import tabulate  # If not installed: pip install tabulate
from datetime import datetime
import getpass
import os

# --- Constants ---
SQUARE_FEET_PER_GALLON = 122
HOURS_PER_GALLON = 8
LABOR_RATE = 47.00

# --- Welcome Message ---
print("\nWelcome to the Paint Job Estimator Program.")
print("This program estimates paint and labor costs for a job based on wall size and paint cost.")

# --- Function: Perform calculations ---
def estimate_paint_job(square_feet, price_per_gallon):
    gallons_needed = math.ceil(square_feet / SQUARE_FEET_PER_GALLON)
    labor_hours = gallons_needed * HOURS_PER_GALLON
    paint_cost = gallons_needed * price_per_gallon
    labor_cost = labor_hours * LABOR_RATE
    total_cost = paint_cost + labor_cost
    return gallons_needed, labor_hours, paint_cost, labor_cost, total_cost

# --- Function: Create unique output filename ---
def generate_output_filename():
    """Generates a unique filename based on datetime and user."""
    username = getpass.getuser()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"paintestimate_{timestamp}_{username}.txt"

# --- Function: Format values for alignment ---
def format_output(gallons, hours, paint_cost, labor_cost, total_cost):
    """Formats numerical values for alignment on decimal places."""
    return [
        ["Gallons of paint required", f"{gallons:>10d}"],
        ["Hours of labor required",   f"{hours:>10.1f}"],
        ["Cost of the paint",         f"${paint_cost:>9.2f}"],
        ["Labor charges",             f"${labor_cost:>9.2f}"],
        ["Total cost of the job",     f"${total_cost:>9.2f}"]
    ]

# --- Function: Print and save results ---
def display_and_save_results(gallons, hours, paint_cost, labor_cost, total_cost, filename):
    """Prints and writes aligned results using tabulate."""
    table_data = format_output(gallons, hours, paint_cost, labor_cost, total_cost)

    print("\nPaint Job Estimate")
    print(tabulate(table_data, headers=["Item", "Amount"], tablefmt="grid", colalign=("left", "right")))

    try:
        with open(filename, 'a') as f:
            f.write("\nPaint Job Estimate\n")
            f.write(tabulate(table_data, headers=["Item", "Amount"], tablefmt="grid", colalign=("left", "right")))
            f.write("\n\n")
        print(f"\nEstimate saved to: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"Error writing to output file: {e}")

# --- Main Program Loop ---
try:
    while True:
        square_feet = pyip.inputFloat("\nEnter total square feet of wall space: ", min=0.1)
        price_per_gallon = pyip.inputFloat("Enter price per gallon of paint: $", min=0.01)

        gallons, hours, paint_cost, labor_cost, total = estimate_paint_job(square_feet, price_per_gallon)

        output_file = generate_output_filename()

        display_and_save_results(gallons, hours, paint_cost, labor_cost, total, output_file)

        again = pyip.inputYesNo("\nWould you like to estimate another paint job? (yes/no): ")
        if again == 'no':
            print("\nThank you for using the Paint Job Estimator.")
            break

except KeyboardInterrupt:
    print("\nProgram interrupted by user.")