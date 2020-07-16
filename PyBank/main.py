#The total number of months in dataset
#The net total amount of profit/losses over the netire period
#The average of the changes in profit/losses over the entire period
#The greatest increase in profits(data&amount) over entire period
#The greatest decrease in losses(data&amount) over entire period

import os
import csv

csvpath = os.path.join(".", "PyBank","Resources","budget_data.csv")
analysis = os.path.join(".", "PyBank","Resources","Analysis.txt")

#Set the variables 
totalAmount = 0
totalMonths = 0
profitLoss_change = 0
profitLoss_prev = 0
profitLoss_change = []
profitLost_Total_Change = 0
greatest_Inc = ['',0]
greatest_Dec = ['',0]

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
        profitLoss_change = int(row["Profit/Losses"]) - profitLoss_prev
        if profitLoss_prev == 0:
                profitLoss_change = 0
        
        profitLost_Total_Change += profitLoss_change
        profitLoss_prev = int(row["Profit/Losses"])

# Greatest Increase
        if profitLoss_change > greatest_Inc[1]:
                greatest_Inc[0] = row['Date']
                greatest_Inc[1] = profitLoss_change
       
# Greatest Decrease
        if profitLoss_change < greatest_Dec[1]:
                greatest_Dec[0] = row['Date']
                greatest_Dec[1] = profitLoss_change
       
profitLoss_Total_Avg = profitLost_Total_Change/(totalMonths-1)

# Set print statements outside of loop to output totals
output = ('\nFinancial Analysis'
'\n----------------------------'        
f'\nThe total number of months: {totalMonths}'
f'\nThe total amount: ${totalAmount:,.2f}'       
f'\nThe changes in Profit/Losses: ${profitLoss_Total_Avg:,.2f}'
f'\nGreatest Increase in Profits: {greatest_Inc[0]} (${greatest_Inc[1]:,.2f})'
f'\nGreatest Decrease in Profits: {greatest_Dec[0]} (${greatest_Dec[1]:,.2f})')

print(output)

with open(analysis,'w') as output_text:
        output_text.write(output)





