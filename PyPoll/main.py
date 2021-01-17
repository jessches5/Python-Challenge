#Modules
import os
import csv
import statistics

#Set path for file
file_csv = os.path.join(".","Resources", "election_data.csv")

#Lists to store data
votes = []
total_votes = []
counties = []
candidates = []
length = []
Khan_votes = []
Correy_votes = []
Li_votes = []
OTooley_votes = []
#Use encoding for Windows
with open(file_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Read the header row first
    csv_header = next(csv_file)

    #Loop through
    for row in csv_reader:

        #Append Columns
        total_votes.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])

        #Total votes
        total_votes = += 1
		if (row[2]) == "Khan"):
            Kahn_votes += 1
        
        elif (row[2]) == "Correy"):
            Correy_votes += 1
        
        elif (row[2]) == "Li"):
            Li_votes += 1
        else (row[2]) == "O'Tooley"
            OTooley_votes += 1

        #Total percentages
        Khan_Percentage = (Khan_votes / total_votes) * 100

        Correy_Percentage = (Correy_votes / total votes) * 100

        Li_Percentage = (Li_votes/ total votes) * 100

        OTooley_Percentage = (OTooley_votes) * 100

        #Winner
        Winning_Candidate = max(Khan_votes, Correy_votes, Li_votes, OTooley_votes)

        if Winning_Candidate == "Khan"
            Winner = "Khan"
        
        elif Winning_Candidate == "Correy"
            Winner = "Correy"

        elif Winning_Candidate == "Li"
            Winner = "Li"

        else Winning_Candidate == "O'Tooley"
            Winner = "O'Tooley
        
        print("Election Results")
		print("-----------------------------------------")
        print(f"Total Votes: {total_votes}")
        print("-----------------------------------------")
        print(f"Khan: {Khan_Percentage: .3%}({Khan_votes})")
        print(f"Correy: {Correy_Percentage: .3%}({Correy_votes})")
        print(f"Li: {Li_Percentage: .3%} ({Li_votes})")
        print(f"O'Tooley: {OTooley_Percentage: .3%} ({OTooley_votes})")
        print("------------------------------------------")
        print(f"Winner: {Winner})
        print("------------------------------------------")
      

output_file = os.path.join("pypoll_final.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)