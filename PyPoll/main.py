
import os
import csv

csvpath = os.path.join(".","PyPoll","Resources","election_data.csv")
pollAnalysis = os.path.join(".", "PyPoll","Resources","analysis.txt")

#Set the variables, list and dictionary
totalVotes = 0
candidatesList = []
candidatesVote = {}

with open (csvpath) as csvfile:
    csvreader=csv.DictReader(csvfile, delimiter=',')

#run the following code to skip the header values
    # csv_header=next(csvreader, None)

    for row in csvreader:
    #     print(row['Candidate'])
        totalVotes = totalVotes +1
    
# Create a list of candidates and number of received votes
        name = row['Candidate']
        if name not in candidatesList:
            candidatesList.append(name)
            candidatesVote[name] = 0
        
        candidatesVote[name] += 1

# print (candidatesList[0])
output = (f'\nElection Results\n'
            '----------------------------------------\n'
            f'The total number of votes: {totalVotes}\n'       
            '----------------------------------------\n')

for name in candidatesList:
    output += f'{name}: {candidatesVote[name]/totalVotes*100:.3f}% ({candidatesVote[name]})\n'  
print(output)
print ('----------------------------------------')
winner = candidatesList[0]
print (f'Winner: {winner}')


with open(pollAnalysis,'w') as output_text:
        output_text.write(output)