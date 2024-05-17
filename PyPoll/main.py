import os
import csv

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

totalvotes = 0
candidatevotes = {}
Charles_Casper_Stockham = 0
Diana_DeGette = 0
Raymon_Anthony_Doane = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:
        totalvotes += 1
        candidatename = row[2]
        
        if "Charles" in candidatename:
            Charles_Casper_Stockham += 1
        elif "Diana" in candidatename:
            Diana_DeGette += 1
        elif "Raymon" in candidatename:
            Raymon_Anthony_Doane += 1

first = (Charles_Casper_Stockham / totalvotes) * 100
second = (Diana_DeGette / totalvotes) * 100
third = (Raymon_Anthony_Doane / totalvotes) * 100

candidatevotes = {"Charles Casper Stockham": Charles_Casper_Stockham,"Diana DeGette": Diana_DeGette,"Raymon Anthony Doane": Raymon_Anthony_Doane}

winner = max(candidatevotes, key=candidatevotes.get)
     
print("Election Results:")
print(f"Total Votes: {totalvotes}")
print("Charles Caspar Stockham:", first, Charles_Casper_Stockham)
print("Diana DeGette:", second, Diana_DeGette)
print("Raymon Anthony Doane:", third, Raymon_Anthony_Doane)
print("Winner:", winner)

output_file = "analysis.txt"

with open(output_file, "w") as file:
    file.write("Election Results:")
    file.write(f"Total Votes: {totalvotes}")
    file.write(f"Charles Caspar Stockham: {first}, {Charles_Casper_Stockham}")
    file.write(f"Diana DeGette: {second}, {Diana_DeGette}")
    file.write(f"Raymon Anthony Doane: {third}, {Raymon_Anthony_Doane}")
    file.write(f"Winner: {winner}")