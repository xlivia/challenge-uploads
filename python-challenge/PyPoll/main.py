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

# Print Statements

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = votes / total_votes * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Output The Results To A File

output_file = "analysis/election_results.txt"

with open(output_file, 'w') as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = votes / total_votes * 100
        outfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-------------------------")
