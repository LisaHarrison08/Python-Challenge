import os
import csv

csvpath = "/Users/LmH80/Desktop/DataViz/Homework/Python-Challenge/PyPoll/Resources/election_data.csv"

with open (csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)

    for row in csvreader:
        print(row)
        