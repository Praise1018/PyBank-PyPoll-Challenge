import os
import csv

csvpath = os.path.join("PyBank/Resources/budget_data.csv")

totalmonths = 0
totalmonths += 0
nettotal = 0
averagechange = 0
greatestincrease = 0
greatestdecrease = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    for row in csvreader:
       
       totalmonths += 1
       nettotal += int(row[1])

       greatestincrease = max(row[1])
       greatestdecrease = min(row[1])
       
averagechange = round(nettotal/totalmonths)

print(f"Total Months: {totalmonths}")
print(f"Total: ${nettotal}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase: {greatestincrease}")
print(f"Greatest Decrease: {greatestdecrease}")

output_file = "analysis.txt"

with open(output_file, "w") as file:
    file.write(f"Total Months: {totalmonths}")
    file.write(f"Total: ${nettotal}")
    file.write(f"Average Change: ${averagechange}")
    file.write(f"Greatest Increase: {greatestincrease}")
    file.write(f"Greatest Decrease: {greatestdecrease}")


