#The total number of months in dataset
#The net total amount of profit/losses over the netire period
#The average of the changes in profit/losses over the entire period
#The greatest increase in profits(data&amount) over entire period
#The greatest decrease in losses(data&amount) over entire period

import os
import csv
#defaultdict knows to expect integers as values and starts at 0
# from collections import defaultdict

csvpath = os.path.join(".","PyBank","Resources","budget_data.csv")

#Set the variables - later update to counts=defaultdict(int)?
totalAmount = 0
totalMonths = 0
profitLoss_change = 0
profitLoss_prev = 0
profitLoss_change = []

#Read the csv file and initialize DictReader for csv key value pairs
with open(csvpath) as budget:
    csvreader = csv.DictReader(budget, delimiter=',')
    # print(csvreader)

# Set file to output a written analysis to a text file

#run the following code to view the header values
    # csvheader = next(csvreader)
    # print(f'CSV_Header:{csvheader}')

#Do not need to run the following code to skip the header values as using DictRead
    # csv_header=next(csvreader, None)

# Loop through data and calculate the totals
    for row in csvreader:
        totalMonths = totalMonths +1
        profitLoss = int(row["Profit/Losses"])

#Calculate the total amount profit/losses += increments the row
        totalAmount += int(row["Profit/Losses"])

#Track the changes in profit/losses over the entire period - += increments each PL row
        profitLoss_prev += int(row["Profit/Losses"])
        profitLoss_change = int(row["Profit/Losses"]) - profitLoss_prev

#Calculate the average of the changes in profit/losses over the entire period      
        average = totalAmount/totalMonths
# Round the average amount to two decimal places
        average = round (average,2)

# Do I need to track the months to then calculate the following and store in a list - months[] is this a calculation of greatest over the year or the entire data set?

#The greatest increase in profits(data&amount) over entire period

#The greatest decrease in losses(data&amount) over entire period

# Set print statements outside of loop to output totals        
print(f'The total number of months:{totalMonths}')
print(f'The total amount:{totalAmount}')       
print(f'The changes in Profit/Losses:{profitLoss_change}')
print(f'The average changes in Profit/Losses:{average}')



