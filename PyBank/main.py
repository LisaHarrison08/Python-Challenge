import os
import csv

csvpath = "/Users/LmH80/Desktop/DataViz/Homework/Python-Challenge/PyBank/Resources/budget_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    for row in csvreader:
        #print(row)

        #totalMonths = row[0]
        #print(totalMonths)

        # amountProfit = row[1]
        # print(amountProfit)


