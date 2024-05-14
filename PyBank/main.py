import os
import csv

csvpath = os.path.join("PyBank/Resources/budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csvheader = next(csvreader)
    
    print(f"CSV Header: {csvheader}")

    for row in csvreader:

        print(row)