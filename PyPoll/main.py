#pyPoll

import pandas as pd

df = pd.read_csv('PyPoll/Resources/election_data.csv')
total_votes = df['Ballot ID'].count()
candidates = df['Candidate'].unique()
print(total_votes)
print(candidates)
c_vote = df['Candidate'].value_counts(normalize=True)
print(c_vote)