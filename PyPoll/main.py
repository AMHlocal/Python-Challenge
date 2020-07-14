#Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# The dataset is composed of three columns: Voter ID, County, and Candidate.

#Dependencies
import os
import csv

#Specify the file to pull from
csvpath = os.path.join('Resources', 'election_data.csv')

#Variables, lists, and dictionary
votes = 0
candidate_list = [] #list to track number of times candidate occurs
election_result = {}
keys = []
values = []
#Open CSV and read headers
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    #print(f"Header: {csvheader}") #headers: Voter ID = 0, County = 1, Candidate = 2

#Loop through data
    for row in csvreader:
        votes += 1 #Counts total number of votes. 
        candidate = row[2] #gets just the candidate away from the other columns.
                           #since print will show what each person voted for we now have to add up all of those votes
        if candidate not in election_result: #adds up how many times the candidate is in row [2], puts them into a dictionary
            election_result[candidate] = 1
        else:
            election_result[candidate] +=1

    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {votes}")
    print("--------------------")
    for candidates, result in election_result.items(): #takes the election_results dictionary and turns the canadiates and results into workable items
        print("%s : %.3f" % (candidates, (result/ votes)*100) + "%" + " " + "(" + str(result) + ")") #prints out the canadiate,
                                                                                                     # % of vote they got, and total number of votes they got 
    for key, value in election_result.items():
        keys.append(key) #takes the names of candidates and puts them into the key list
        values.append(value) #takes the amount of times they were voted and put them into the values list
    #locate highest value from value list
    highest_value = max(values)
    #locate canadiate with most votes, by index
    most_votes = values.index(highest_value)
    #get name from the index
    name = keys[most_votes]
    print("--------------------")
    print(f"Winner: {name}")
    print("--------------------")
    
#write to a text file
analysis = os.path.join("Analysis", "PyPoll_Analysis.txt")
with open(analysis, "w") as output:
    output.write("Election Results\n")
    output.write("--------------------\n")
    output.write(f"Total Votes: {votes}\n")
    output.write("--------------------\n")
    for candidates, result in election_result.items():
        output.write("%s : %.3f" % (candidates, (result/ votes)*100) + "%" + " " + "(" + str(result) + ")\n")
    output.write("--------------------\n")
    output.write(f"Winner: {name}\n")
    output.write("--------------------\n")
