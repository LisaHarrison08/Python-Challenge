#The total number of months in dataset
#The net total amount of profit/losses over the netire period
# ---- totalPl_amount = sum int(row[2])
    #print (totalPl_amount)
#The average of the changes in profit/losses over the entire period
#--- def average (row[2])
        #averageP_L =sum(row[2])/len(row[2])
        #return averageP-L

#The greatest increase in profits(data&amount) over entire period
#The greatest decrease in losses(data&amount) over entire period

import os
import csv

csvpath = os.path.join(r"/Users/LmH80/Desktop/DataViz/Homework/Python-Challenge/PyBank/Resources/budget_data.csv")

# #Set the variables
# # totalAmount = 0
# totalMonths = 0

#Read the csv file
with open(csvpath) as budget:
    csvreader = csv.reader(budget, delimiter=',')
    print(csvreader)

#run the following code to view the header values
    csvheader = next(csvreader)
    print(f'CSV_Header:{csvheader}')

#run the following code to skip the header values
    # csv_header=next(csvreader, None)

    # for row in csvreader:
        #print(row)
         #months = row[0]
        # totalMonths = totalMonths +1
        # profitLoss = int(row[1])
        # print(profitLoss)

# calculate the total number of months
        # numberMonths += months
        # print (totalMonths)

#calculate the total amount profit/losses
        # totalAmount += int(profitLoss)
#print(f'The total number of months:{totalMonths}')
#print(f'The total amount:{totalAmount}')       



