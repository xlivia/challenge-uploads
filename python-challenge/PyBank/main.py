# budget_data.csv

import csv

total_months = 0
total_price = 0
average_change = 0.00
greatest_inc = ""
greatest_dec = ""
max_profit_price = 0
min_profit_price = 0

idx = 0
budget = {
    "idx": {
        "month": "",
        "year": 0,
        "price": 0.00
    }
}

budget_data = []

# Read Resources/buget_data.csv

fpath ="Resources/budget_data.csv"

with open(fpath, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',') # make the csv file readable
    next(csvreader, None) # skip the header row
    for row in csvreader: # loop through each row of csv file
        budget = dict(month = str(row[0][0] + row[0][1] + row[0][2]), year = int(row[0][4] + row[0][5]), price = int(row[1]))
        budget_data.append(budget)
        idx += 1
        total_months += 1 # add the total months
        total_price += int(row[1]) # add the total price
        if (max_profit_price < int(row[1])):
            max_profit_price = int(row[1])
            greatest_inc = row[0] + " (" + str(max_profit_price) + ")"
        if (min_profit_price > int(row[1])):
            min_profit_price = int(row[1])
            greatest_dec = row[0] + " (" + str(min_profit_price) + ")"

#curr_year_sum = 0
#i = 0
#while i < len(budget_data):
#    curr_year = budget_data[i]["year"]
#    print(curr_year)
#    while curr_year == budget_data[i]["year"]:
#        curr_year_sum += int(budget_data[i]["price"])
#    i += 1

average_change = total_price / total_months

# Print Outputs

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}") # 86
print(f"Total: ${total_price}") # 22564198
print(f"Average Change: ${average_change}") # -8311.11
print(f"Greatest Increase in Profits: {greatest_inc}") # Aug-16 ($1862002)
print(f"Greatest Decrease in Profits: {greatest_dec}") # Feb-14 ($-1825558)
