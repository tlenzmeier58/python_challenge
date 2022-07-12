import os
import csv

# path to collect data
pybank = os.path.join('Resources', 'budget_data.csv')


profit = []
monthly_changes = []
date = []

count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

with open(pybank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # get the data
    for row in csvreader:

        # use count to get the number of months
        count = count + 1

        # we will use this for capturing the greatest increase/decrease
        date.append(row[0])

        profit.append(row[1])
        total_profit = total_profit + int(row[1])
        currency = "${:,.2f}".format(total_profit)

        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        # store montly changes in a list
        monthly_changes.append(monthly_change_profits)
        
        # calculate the total change
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        # calculate the average change
        average_change_profits = (total_change_profits/count)

        # the max/min of profits
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        # capture the date where the greatest increase/decrease occured
        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
    
    print(" ")
    print("Financial Analysis")
    print("-------------------------------------")
    print("Total Profits: " + str(currency))
    print("Total Months: " + str(count))
    print("Average Change: " + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")")

with open('financial_analysis.txt', 'w') as text:
    text.write("  \n")
    text.write("Financial Analysis" + "\n")
    text.write("------------------------------------------------\n\n")
    text.write("  Total Months: " + str(count) + "\n")
    text.write("  Total Profits: " + "$" + str(total_profit) + "\n")
    text.write("  Average Change: " + "$" + str(int(average_change_profits)) + "\n")
    text.write("  Greatest Increase In Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("  Greatest Decrease In Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")


     