# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("budget_data.csv")
txtFile = os.path.join("budget_results.txt")
# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    
    monthCount = 0
    netTotal = 0 
    changeList = 0
    greatestIncrease = 0
    leastIncrease = 0
    greatestDate = ""
    leastDate = ""
    
    first = next(csvreader)
    monthCount += 1
    netTotal += int(first[1])
    monthBeforeProfit = int(first[1])
    print(monthBeforeProfit)

    
    
    for row in csvreader:
        monthCount += 1
        netTotal += int(row[1])
        change = int(row[1]) - monthBeforeProfit
        if (change > greatestIncrease):
            greatestIncrease = change
            greatestDate = row[0]
        if (change < leastIncrease):
            leastIncrease = change
            leastDate = row[0]
        changeList = changeList + change
        monthBeforeProfit = int(row[1])




averageChangeList = changeList/(monthCount - 1)

print ("Financial Analysis \n -------------------------------")
print(f"Total Months: {monthCount}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${averageChangeList:.2f}")
print(f"Greatest Increase in Profits: {greatestDate} (${greatestIncrease})")
print(f"Greatest Decrease in Profits: {leastDate} (${leastIncrease})")

results = (f"Financial Analysis \n" f"-------------------------------\n" f"Total Months: {monthCount}\n"
    f"Total: ${netTotal}\n" f"Average Change: ${averageChangeList:.2f}\n" f"Greatest Increase in Profits: {greatestDate} (${greatestIncrease})\n"
        f"Greatest Decrease in Profits: {leastDate} (${leastIncrease})")

with open(txtFile, 'w') as txt:
    txt.write(results)
    