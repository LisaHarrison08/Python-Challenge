
import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
pollAnalysis = os.path.join("Resources","analysis.txt")

#Set the variables, list and dictionary
totalVotes = 0
candidatesList = []
candidatesVote = {}

with open (csvpath) as csvfile:
    csvreader=csv.DictReader(csvfile, delimiter=',')

#run the following code to view the header values
    # csvheader = next(csvreader)
    # print(f'CSV_Header:{csvheader}')

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
# print(candidatesVote.keys())
#Calculate the winner 
    for key in candidatesVote.keys():
        if candidatesVote[key] == max(candidatesVote.values()):
            winner = key
    # print(winner)

output = (f'\nElection Results\n'
            '----------------------------------------\n'
             f'Winner: {winner}\n'       
            '----------------------------------------\n'
            f'The total number of votes: {totalVotes}\n'       
            '----------------------------------------\n')
for name in candidatesList:
    output += f'{name}: {candidatesVote[name]/totalVotes*100:.3f}% ({candidatesVote[name]})\n'  
print(output)

with open(pollAnalysis,'w') as output_text:
        output_text.write(output)