#pyPoll

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
import csv
from collections import Counter

total_vote =0
candidates =[]


with open('PyPoll/Resources/election_data.csv', 'r') as f:
  reader = csv.reader(f)
  header = next(reader)
  for row in reader:
    total_vote +=1
    candidates.append(row[2])
vote = Counter(candidates)

print('Election Results')
print('-------------------------')
print('Total Votes: ')
print('-------------------------')
print('for loop')
print('-------------------------')
print('Winner: ')
print('-------------------------')