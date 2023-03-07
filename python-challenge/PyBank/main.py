# budget_data.csv

import csv

total_months = 0
total_price = 0
average_change = 0.00
inc_prof = ""
dec_prof = ""

# Read Resources/buget_data.csv

fpath ="Resources/budget_data.csv"

with open(fpath, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',') # make the csv file readable
    next(csvreader, None) # skip the header row
    for row in csvreader: # loop through each row of csv file
        # print(row[0], row[1]) # print each row of csv file
        total_months += 1 # add the total months
        total_price += int(row[1]) # add the total price

# Print Outputs

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}") # 86
print(f"Total: ${total_price}") # 22564198
# print(f"Average Change: ${average_change}") # -8311.11
# print(f"Greatest Increase in Profits: {inc_prof}") # Aug-16 ($1862002)
# print(f"Greatest Decrease in Profits: {dec_prof}") # Feb-14 ($-1825558)
