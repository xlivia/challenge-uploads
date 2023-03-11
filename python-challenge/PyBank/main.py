import csv

fpath ="Resources/budget_data.csv" # file path

total_months = 0
total_price = 0
changes = []
dates = []

# Read in the CSV file
with open(fpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') # make the csv file readable
    next(csvreader) # skip the header row
    for row in csvreader: # loop through each row of csv file
        total_months += 1 # add the total months
        dates.append(row[0]) # add the dates to the list
        total_price += int(row[1]) # add the total price
        changes.append(int(row[1])) # add the price changes to the list

average_change = sum(changes) / len(changes)

greatest_inc = max(changes)
greatest_dec = min(changes)
greatest_inc_date = dates[changes.index(greatest_inc)]
greatest_dec_date = dates[changes.index(greatest_dec)]

# Output The Results To A File

output_file = "analysis/results.txt"

with open(output_file, 'w') as outputfile:
    outputfile.write("Financial Analysis\n")
    outputfile.write("----------------------------\n")
    outputfile.write(f"Total Months: {total_months}\n")
    outputfile.write(f"Total: ${total_price}\n")
    outputfile.write(f"Average Change: ${average_change:.2f}\n")
    outputfile.write(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})\n")
    outputfile.write(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})")

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}") #86
print(f"Total: ${total_price}") # 22564198
print(f"Average Change: ${average_change:.2f}") # -8311.11
print(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})") # Aug-16 ($1862002)
print(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})") # Feb-14 ($-1825558)
