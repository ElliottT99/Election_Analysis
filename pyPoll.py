#List of items we need to retrieve
#imports
import csv
import os

#accessing .csv file to read the results

file_to_load = os.path.join("..", "Resources", "election_results.csv")
file_to_save = os.path.join("..", "analysis", "election_analysis.txt")

#testing writing to files
#outfile = open(file_to_save, "w")
#outfile.write("Hello World")

#retireving data from .csv

#method one for reading data from csv
#election_data = open(file_to_load, r)

#initializing variables
total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#method two for reading data from csv

#with open(file_to_save, "w") as txt_file:
#    txt_file.write("Counties in the Election\n---------------------\nArapahoe\nDenver\nJefferson")

with open(file_to_load) as election_data:
    #to do: analyze data
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    #print(headers)
    
    for row in file_reader:
        #prints each row in csv
        #print(row)
        #add to the total vote count
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        votes_percentage = float(votes)/float(total_votes) * 100
        #print(f'{candidate_name} recieved {votes_percentage:.3}% of the votes')
        candidate_results = (f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (votes_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = votes_percentage
            winning_candidate = candidate_name
            #candidate_results = (f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
        
        print(candidate_results)
        txt_file.write(candidate_results)

#print(total_votes)
#print(candadite_options)
#print(candadite_votes)


    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

#1. total number of votes
#2. list of candadites who recieved votes
#3. percentage of votes for each voter
#4. total number of votes for each candadite
#5. winner of election based on popular votes


#close the files
#outfile.close()
#election_data.close()
