import os
import csv

months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

pybank = os.path.join("Resources", "budget_data.csv")

with open(pybank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read the header row
    csv_header = next(csvreader)

#    print(csv_header)
    for row in csvreader:

        # Count of months
        count_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Compute change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {count_months}")
    print(f"Total Profit/Loss: {net_profit_loss}")
    print(f"Average Change: {average_profit_loss}")
    print(f"Greatest Increase In Profits: {highest_change}")
    print(f"Greatest Decrease In Profits: {lowest_change}")

text_file = os.path.join("financial_analysis.txt")

with open(text_file, "w") as output:
    output.write("Financial Analysis \n")
    output.write("---------------------------\n")
    output.write(f"Total Months: {count_months}\n")
    output.write(f"Total Profit/Loss: {net_profit_loss}\n")
    output.write(f"Average Changes: {average_profit_loss}\n")
    output.write(f"Greatest Increase In Profits: {best_month} (${highest_change})\n")
    output.write(f"Greatest Decrease In Profits: {worst_month} (${lowest_change}\n")
    output.write("-----  That's a wrap -----------\n")
    
    

