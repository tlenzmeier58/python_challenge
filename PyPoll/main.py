# get modules
import os
import csv
import collections
from collections import Counter

# list for tallying votes
voters_candidate = []
votes_per_candidate = []

# get the data from the relevant director
pypoll = os.path.join("Resources", "election_data.csv")

with open(pypoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # header row
    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")

    # read the data
    for row in csvreader:
        voters_candidate.append(row[2])

    # print(voters_candidate)

    # sort the list
    sorted_list = sorted(voters_candidate)

    # print(sorted_list)

    # arrange the list
    arrange_list = sorted_list

    count_candidate = Counter(arrange_list)
    votes_per_candidate.append(count_candidate.most_common())
    # print(votes_per_candidate)

    # percentage of votes per candidate
    for item in votes_per_candidate:
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())), '.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())), '.3f')
    print(" ")
    print("Election Results")
    print("-----------------------------------------------------")
    print(f"Total Votes:  {sum(count_candidate.values())}")
    print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
    print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
    print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
    print("-----------------------------------------------------")
    print(f"Winner: {votes_per_candidate[0][0][0]}")

    # export to a text file
    output_file = os.path.join("Resources", "election_results.csv")


    with open(output_file, "w") as output:
        output.write(" \n")
        output.write("Election Results\n")
        output.write("-----------------------------------------------------\n")
        output.write(f"Total Votes:  {sum(count_candidate.values())}\n")
        output.write("-----------------------------------------------------\n")
        output.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
        output.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
        output.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
        output.write("-----------------------------------------------------\n")
        output.write(f"Winner: {votes_per_candidate[0][0][0]}\n")
        output.write("------------------------------------------------------\n")




