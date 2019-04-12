# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("election_data.csv")
txtFile = os.path.join("election_results.txt")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)

    total_votes = 0
    candidates = []
    candidate_votes = {}

    for row in csvreader:
        total_votes += 1
        
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1


print ("Election Results \n -------------------------------")
print(f"Total Votes: {total_votes}")
print ("-------------------------------")

mostVotes = candidates[0]

for candidate in candidates:
    percentage = candidate_votes[candidate]/total_votes
    if candidate_votes[candidate] > candidate_votes[mostVotes]:
        mostVotes = candidate
    print(f"{candidate}: {percentage * 100:.3f}% ({candidate_votes[candidate]})")

print ("-------------------------------")
print(f"Winner: {mostVotes}")
print ("-------------------------------")

# results = (f"Financial Analysis \n" f"-------------------------------\n" f"Total Months: {monthCount}\n"
#     f"Total: ${netTotal}\n" f"Average Change: ${averageChangeList:.2f}\n" f"Greatest Increase in Profits: {greatestDate} (${greatestIncrease})\n"
#         f"Greatest Decrease in Profits: {leastDate} (${leastIncrease})")

# with open(txtFile, 'w') as txt:
#     txt.write(results)