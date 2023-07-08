#pyPoll

#import pandas as pd

#df = pd.read_csv('PyPoll/Resources/election_data.csv')
#total_votes = df['Ballot ID'].count()
#candidates = df['Candidate'].unique()
#print(total_votes)
#print(candidates)
#c_vote = df['Candidate'].value_counts(normalize=True)
#print(c_vote)

import csv
with open('PyPoll/Resources/election_data.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    print(row)


print('Election Results')
print('-------------------------')
print('Total Votes: ')
print('-------------------------')
print('for loop')
print('-------------------------')
print('Winner: ')
print('-------------------------')