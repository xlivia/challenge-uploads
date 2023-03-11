import csv

total_votes = 0
candidates = {}
winner = ""

fpath ="Resources/election_data.csv" # file path

with open(fpath, 'r') as csvfile: # read the csv file
    csvreader = csv.reader(csvfile, delimiter=',') # make the cas file readable
    next(csvreader) # Skip the header row
    for row in csvreader: # loop through each row of file
        total_votes += 1 # add the total votes
        candidate_name = row[2] # get the candidates names
        if candidate_name not in candidates: # if candidate is not in dictionary
            candidates[candidate_name] = 0 # add the candidate to the dictionary
        candidates[candidate_name] += 1 # go to next index

max_votes = 0
for candidate, votes in candidates.items():
    if votes > max_votes: # find the max votes
        max_votes = votes
        winner = candidate

# Output The Results To A File

output_file = "analysis/results.txt"

with open(output_file, 'w') as outputfile:
    outputfile.write("Election Results\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Total Votes: {total_votes}\n")
    outputfile.write("-------------------------\n")

    for candidate, votes in candidates.items():
        votes_percent = votes / total_votes * 100
        outputfile.write(f"{candidate}: {votes_percent:.3f}% ({votes})\n")

    outputfile.write("-------------------------\n")
    outputfile.write(f"Winner: {winner}\n")
    outputfile.write("-------------------------")

# Print Statements

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}") # 369711
print("-------------------------")

for candidate, votes in candidates.items():
    votes_percent = votes / total_votes * 100
    print(f"{candidate}: {votes_percent:.3f}% ({votes})")
    # Charles Casper Stockham: 23.049% (85213)
    # Diana DeGette: 73.812% (272892)
    # Raymon Anthony Doane: 3.139% (11606)

print("-------------------------")
print(f"Winner: {winner}") # Diana DeGette
print("-------------------------")
