#  * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

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
        