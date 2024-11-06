# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Files to load and output (update with correct file paths)
input_filepath = os.path.join('Resources/budget_data.csv')  # when parent folder open in Visual Studio Code
  # Output file path
output_file = os.path.join('analysis/budget_analysis.txt')

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
#max and min month will have to be string cause we only need them for the printed analysis at the end and we wont need to do any functions with them
prev_month = 0
current_month = 0
total_change = 0 
max_change = 0
max_month = ""
least_change = 0
least_month = ""

# Open and read the csv
with open(input_filepath) as budget_data:
    reader = csv.reader(budget_data, delimiter= ',')

    # Skip the header row
    header = next(reader)


    # Process each row of data
    for row in reader:
        
        total_months += 1 
        total_net += int(row[1])
        # Track the total

        if total_months == 1 : 
            prev_month = int(row[1])

        # Track the net change
        else: 
            current_month = int(row[1])
            change = current_month - prev_month
            total_change += change 

            prev_month = current_month

        # Calculate the greatest increase in profits (month and amount)
            if change > max_change:
                max_change = change
                max_month = row[0]

        # Calculate the greatest decrease in losses (month and amount)
            if change < least_change:
                least_change = change 
                least_month = row[0]


# Calculate the average net change across the months
average_change = total_change / (total_months - 1)

# Generate the output summary

with open(output_file, "w") as txt_file:

 #triple quotes so the output can be on multiple lines   
    output=f"""
Financial Analysis

Total Months: {total_months}
Total: $ {total_net}
Average Change: $ {round(average_change, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {least_month} (${least_change})
"""

# Print the output
    print(output, file=txt_file)

print(output)     