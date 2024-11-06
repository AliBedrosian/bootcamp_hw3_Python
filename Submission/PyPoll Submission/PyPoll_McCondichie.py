# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Files to load and output (update with correct file paths)
importfile = os.path.join("Resources/election_data.csv")  # Input file path
outputfile = os.path.join("analysis/election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
#there needs to be a dictionary created to keep the candidate name(string/key) connected to the amount of votes
votes_info = {}

# Open the CSV file and process it
with open(importfile) as election_data:
    csvread = csv.reader(election_data, delimiter= ',')

    # Skip the header row
    header = next(csvread)

    # Loop through each row of the dataset and process it
    # candidate should start as 2 because its the third value
    for row in csvread:
        candidate = row[2]

        # Increment the total vote count for each row
        total_votes += 1 

        # Get the candidate's name from the row
        if candidate in votes_info.keys():
            votes_info[candidate] += 1 


        # If the candidate is not already in the candidate list, add them
        else:
           votes_info[candidate] = 1  

#using the .get method to pull the vote amounts from the votes info dictionary based on their key
candidate1_votes = votes_info.get('Charles Casper Stockham')
candidate2_votes = votes_info.get('Diana DeGette')
candidate3_votes = votes_info.get('Raymon Anthony Doane')
#finding the max value in the dictionary, then calling on the key connected to it with .get method
winner = (max(votes_info, key=votes_info.get))

with open(outputfile, "w") as txt_file:
    output = f"""
Election Results

Total Votes: {total_votes}

Charles Casper Stockham: {round((candidate1_votes / total_votes) * 100, 3)}% ({candidate1_votes})
Diana DeGette: {round((candidate2_votes / total_votes) * 100, 3)}% ({candidate2_votes})
Raymon Anthony Doane: {round((candidate3_votes / total_votes) * 100, 3)}% ({candidate3_votes})

Winner: {winner}

"""
    print(output, file=txt_file) 

print(output) 