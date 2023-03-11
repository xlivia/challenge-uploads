# budget_data.csv

import csv

total_months = 0

total_price = 0

diff_change = []
average_change = 0.00

greatest_inc = ""
greatest_dec = ""
max_profit_price = 0
min_profit_price = 0

fpath ="Resources/budget_data.csv" # file "Resources/buget_data.csv"

prev = 0
curr = 0

with open(fpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') # make the csv file readable
    next(csvreader, None) # skip the header row

    for row in csvreader: # loop through each row of csv file

        total_months += 1 # add the total months

        total_price += int(row[1]) # add the total price

        curr = int(row[1]) # set current price
        total_change = curr - prev # find price difference of each
        diff_change.append(int(total_change)) # add each price difference to list
        average_change = total_change / total_months # calculate average change
        prev = curr # set previous price after calculations

        if (max_profit_price < int(row[1])):
            max_profit_price = int(row[1])
            greatest_inc = row[0] + " (" + str(max_profit_price) + ")"
        if (min_profit_price > int(row[1])):
            min_profit_price = int(row[1])
            greatest_dec = row[0] + " (" + str(min_profit_price) + ")"

# Print Outputs

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}") # 86
print(f"Total: ${total_price}") # 22564198
print(f"Average Change: ${average_change}") # -8311.11
print(f"Greatest Increase in Profits: {greatest_inc}") # Aug-16 ($1862002)
print(f"Greatest Decrease in Profits: {greatest_dec}") # Feb-14 ($-1825558)
