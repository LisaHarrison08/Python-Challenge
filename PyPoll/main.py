#  * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

import os
import csv

csvpath = os.path.join(".","PyPoll","Resources","election_data.csv")

#defaultdict knows to expect integers as values and starts at 0
# from collections import defaultdict

#Set the variables - later update to counts=defaultdict(int)?
totalVotes = 0

with open (csvpath) as csvfile:
    csvreader=csv.DictReader(csvfile, delimiter=',')

# Set file to output a written analysis to a text file

#run the following code to skip the header values
    # csv_header=next(csvreader, None)

    for row in csvreader:
    #     print(row['Candidate'])
        totalVotes = totalVotes +1
print(f'The total number of votes:{totalVotes}')       