import os
import csv

pypoll_csv = os.path.join('.', 'Resources', 'election_data.csv')

#initilize the variables
vote_total = 0
candidates = { }
vote_percent = 0
winner = ""
winning_vote = 0


with open(pypoll_csv, 'r') as csvfile:
    
    # split the data on commas, skip header row
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)
    
    # loop through the data, count total votes
    for row in csvreader:
        vote_total += 1
        #if key (candidate name) already in dictionary, add one to its vote count, otherwise:
        #add the candidate as a key, add the first vote as the first position in a value that is formatted as a list
        if row[2] in candidates:
            candidates[row[2]][0] += 1
        else:
            candidates[row[2]] = [1]
    
    #loop through dictionary of candidates adding a second value to the list of values that stores the candidates vote percentage
    #if statement finds the winner
    for candidate, vote in candidates.items():
        vote_percent = round((candidates[candidate][0]  / vote_total * 100), 3)
        candidates[candidate].append(vote_percent)
        if candidates[candidate][1] > winning_vote:
            winning_vote = candidates[candidate][1]
            winner = candidate 

#initalize a list to hold individual candidates stats summaries
indv_stats = []

#draft output info, then print to terminal and export to file. 
def election_results():
    total = f"Election Results \n---------------------------- \nTotal Votes: {vote_total} \n----------------------------------\n"
    for candidate, vote in candidates.items():
        indv_stats.append(f"{candidate}: {candidates[candidate][1]}% ({candidates[candidate][0]}) \n" )
    won = f"---------------------------- \nWinner: {winner} \n----------------------------"
    return total + ''.join(indv_stats) + won

elect_resul = election_results()

print(elect_resul)

with open('ele_results.txt', 'w') as f:
    f.write(elect_resul)
 