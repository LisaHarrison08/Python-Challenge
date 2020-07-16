#  * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

import os
import csv

csvpath = os.path.join(".","PyPoll","Resources","election_data.csv")

#Set the variables
totalVotes = 0
candidatesList = []
candidates = {}

with open (csvpath) as csvfile:
    csvreader=csv.DictReader(csvfile, delimiter=',')

#run the following code to skip the header values
    # csv_header=next(csvreader, None)

    for row in csvreader:
    #     print(row['Candidate'])
        totalVotes = totalVotes +1

# Create a list of candidates who received votes
        candidate = row['Candidate']
        if candidate not in candidatesList:
            candidatesList.append(candidate)
            candidates[candidate] = 0
        
        candidates[candidate] += 1

output = (f'\nElection Results\n'
            '----------------------------------------\n'
            f'The total number of votes: {totalVotes}\n'       
            '----------------------------------------\n')

for candidate in candidatesList:
    output += f'{candidate}: {candidates[candidate]/totalVotes*100:.3f}% ({candidates[candidate]})\n'

print(output)