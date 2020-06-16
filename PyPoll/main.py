import os
import csv

#
csv_path = os.path.join("Resources","election_data.csv")

#setup a dictionary
poll_results={}


#Initialiaze the vote counter to zero
#vote_cntr = 0

with open(csv_path) as csvfile
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip over the header
    next(csvreader)
    #get the length minus the header and use as the total number of votes cast
    total_votes_cast = len(list(csvreader))


with open(csv_path) as csvfile
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip over the header
    next(csvreader)
    for row in csvreader:
        if row[2] in poll_results.keys():
            poll_results[row[2]] =  poll_results[row[2]] + 1
        else:
            poll_results[row[2]] = 1

candidate_list[]
total_number_of_votes = []
#loop through the key value pairs in my dict
for key, value in poll_results.items():
    #add key to my candidate list 
    candidate_list.append(key)
    #add the value to my total number of votes list
    total_number_of_votes.append(value)

#Calculate the percentage of votes for each candidate
percentage_of_votes_received = []
for p in total_number_of_votes:
    percentage_of_votes_received =((p/total_votes_cast)*100)


#Smash my new lists together
final_list =  list(zip(candidate_list, toal_number_votes,percentage_of_votes_received))
 
 winner_winner_chicken_dinner = []
for candidate in final_list:
    if max(total_number_of_votes) == candidate[1]
        winner_winner_chicken_dinner.append(candidate[0])
Potus = winner_winner_chicken_dinner[0]
    
print("Election Results")
print("------------------------------------")
print("Total Votes"+ total_votes_cast)
print("------------------------------------")
print
