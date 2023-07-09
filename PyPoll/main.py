#pyPoll

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import csv
total_votes =0
candidates ={}

# read the file
with open('PyPoll/Resources/election_data.csv', 'r') as f:
  reader = csv.reader(f)
  header = next(reader)
  for row in reader:
    total_votes +=1
    if row[2] in candidates:
      candidates[row[2]] += 1
    else:
      candidates[row[2]] = 1

winner = max(candidates,key=candidates.get)

#print to terminal
print('Election Results')
print('-------------------------')
print('Total Votes:',total_votes)
print('-------------------------')

for candidate, vote in candidates.items():
  vote_perc= round((vote/ total_votes) * 100,3)
  print(candidate,':',vote_perc,'% (',vote,')')

print('-------------------------')
print('Winner:',winner)
print('-------------------------')

#write to file
with open('PyPoll/analysis/PyPoll_analysis.txt', 'w') as file:
    file.write('Election Results\n')
    file.write('-------------------------\n')
    file.write('Total Votes: '+ str(total_votes) +'\n')
    file.write('-------------------------\n')
    
    for candidate, vote in candidates.items():
      vote_perc= round((vote/ total_votes) * 100,3)
      file.write(str(candidate) + ': ' + str(vote_perc) + '% (' +str(vote) + ')\n' )
    
    file.write('-------------------------\n')
    file.write('Winner:'+ str(winner)+'\n')
    file.write('-------------------------\n')