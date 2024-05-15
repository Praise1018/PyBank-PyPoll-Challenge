import os
import csv

csvpath = os.path.join("PyBank/Resources/budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

print("Financial Analysis")

print("----------------------------")

