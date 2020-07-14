import os
import csv

csvpath = "/Users/LmH80/Desktop/DataViz/Homework/Python-Challenge/PyBank/Resources/budget_data.csv"

with open(csvpath) as budget:
    csvreader = csv.reader(budget, delimiter=',')
    print(csvreader)

#run the following code to view the header values
    # csvheader = next(csvreader)
    # print(f'CSV_Header:{csvheader}')

#run the following code to skip the header values
    csv_header=next(csvreader, None)

    for row in csvreader:
        print(row[0])
#calculate number of months in the data list

# calculate the total number of months
    # for row in csvreader:
    #     # months = row[0]
    #     # totalMonths = len(months)
    #     # print(totalMonths)
    # #     totalMonths = len(row[0])
    # #     print (totalMonths)

    #     # print(f"Number of months in data:  ,"(totalMonths))
    #     months = row[0]
    #     totalMonths = len(months)
    #     print(totalMonths)

        # amountProfit = row[1]
        # print(amountProfit)


