# -----------------------------------------
# file1
# Author: Lauren Ryman
# Date: 3/8/2025
# Description: This program will read the file numbers.txt, sum the numbers and provide the average
# -----------------------------------------

#Check if file exists
import os
filename = "numbers.txt"

if not os.path.exists(filename):
   print("File does not exist.")
else:
   # Open the file
   file = open(filename, 'r')
   data = file.read().strip()
   # Close the file
   file.close()

   if not data:
      print("File was empty.")
   else:
      numbers_str = data.split()
      total = 0
      count = 0
      for num_str in numbers_str:
         try:
            number = int(num_str)
            total += number
            count += 1
         except ValueError:
            print(f"Warning: '{num_str}' is not a valid integer, skipping.")

      if count > 0:
         average = total / count
         print("Total:", total)
         print("Average:", average)
      else:
         print('No valid numbers found.')