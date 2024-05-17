import os
import csv

csvpath = os.path.join("PyBank/Resources/budget_data.csv")

totalmonths = 0
nettotal = 0
changes = []
dates = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    for row in csvreader:
       
       totalmonths += 1
       nettotal += int(row[1])
       changes.append(int(row[1]))
       dates.append(row[0])

    changevalues = [changes[i+1] - changes[i] for i in range(len(changes)-1)]
    
    if changevalues:
        averagechange = round(sum(changevalues) / len(changevalues))
        greatestincrease = max(changevalues)
        greatestincreasedate = dates[changevalues.index(greatestincrease) + 1]
        greatestdecrease = min(changevalues)
        greatestdecreasedate = dates[changevalues.index(greatestdecrease) + 1]
    else:
        averagechange = 0
        greatestincrease = 0
        greatestincrease_date = ""
        greatestdecrease = 0
        greatestdecrease_date = ""

print("Financial Analysis")
print(f"Total Months: {totalmonths}")
print(f"Total: ${nettotal}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase: {greatestincreasedate}, {greatestincrease}")
print(f"Greatest Decrease: {greatestdecreasedate}, {greatestdecrease}")

output_file = "analysis.txt"

with open(output_file, "w") as file:
    file.write("Financial Analysis")
    file.write(f"Total Months: {totalmonths}")
    file.write(f"Total: ${nettotal}")
    file.write(f"Average Change: ${averagechange}")
    file.write(f"Greatest Increase: {greatestincreasedate}, {greatestincrease}")
    file.write(f"Greatest Decrease: {greatestdecreasedate}, {greatestdecrease}")


