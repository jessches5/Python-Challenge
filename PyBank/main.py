#Modules
import os
import csv
import statistics
#Set path for file
file_csv = os.path.join(".","Resources", "budget_data.csv")

#Lists to store data
total_months = []
total_prof_loss = []
changes = []
greatest_increasae = []
greatest_decrease = []
length = []

#Use encoding for Windows
with open(file_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Read the header row first
    csv_header = next(csv_file)

    #Loop through
    for row in csv_reader:

        #Add date
        total_months.append(row[0])

        #Add profit/losses
        total_prof_loss.append(int(row[1]))

        #Total number of months
        months = len(total_months)
       
    #Net profit/losses
    net_prof_loss = sum(total_prof_loss)

    #Average changes
    avg_prof_loss = net_prof_loss / monthsmax_prof_loss = max(total_prof_loss)

    min_prof_loss = min(total_prof_loss)
    
    print(f"Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${net_prof_loss}")
    print(f"Average Change: ${avg_prof_loss}")
    print(f"Greatest Increase in Profits: Feb-2012 (${max_prof_loss})")
    print(f"Greatest Decrease in Profits: Sept-2013 (${min_prof_loss})")
    

output_file = os.path.join("pybank_final.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)