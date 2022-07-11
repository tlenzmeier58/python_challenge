import os
import csv

# path to collect data
pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        total = 0
        total += int(row[1])
    print(total)



