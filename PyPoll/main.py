import os
import csv

csvpath = "/Users/LmH80/Desktop/DataViz/Homework/Python-Challenge/PyPoll/Resources/election_data.csv"

#Set the variables
totalVotes = 0

with open (csvpath) as csvfile:
    csvreader=csv.DictReader(csvfile, delimiter=',')

#run the following code to skip the header values
    csv_header=next(csvreader, None)

    for row in csvreader:
    #     print(row['Candidate'])
       totalVotes +=1
    print (totalVotes) 
        