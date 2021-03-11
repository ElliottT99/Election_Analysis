#List of items we need to retrieve
#imports
import csv
import os

#accessing .csv file to read the results

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

#testing writing to files
#outfile = open(file_to_save, "w")
#outfile.write("Hello World")

#retireving data from .csv

#method one for reading data from csv
#election_data = open(file_to_load, r)

#method two for reading data from csv

#with open(file_to_save, "w") as txt_file:
#    txt_file.write("Counties in the Election\n---------------------\nArapahoe\nDenver\nJefferson")

with open(file_to_load, "r") as election_data:
    #to do: analyze data
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
#    for row in file_reader:
#        print(row)



#1. total number of votes
#2. list of candadites who recieved votes
#3. percentage of votes for each voter
#4. total number of votes for each candadite
#5. winner of election based on popular votes


#close the files
#outfile.close()
#election_data.close()
