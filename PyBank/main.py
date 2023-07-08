#PyBank
#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period


import pandas as pd

df = pd.read_csv('python-challenge/PyBank/Resources/budget_data.csv')

total_months = df['Date'].count()
net_total = df['Profit/Losses'].sum()
max_total = df['Profit/Losses'].max()
min_total = df['Profit/Losses'].min()
avg_total = round(df['Profit/Losses'].mean(),2)
max_date = df.loc[df['Profit/Losses'].idxmax(),'Date']
min_date = df.loc[df['Profit/Losses'].idxmin(),'Date']

print('Financial Analysis')
print('----------------------------')
print('Total Months:',total_months)
print('Total:',net_total)
print('Average Change: $',avg_total)
print('Greatest Increase in Profits: ',max_date,max_total)
print('Greatest Decrease in Profits: ',min_date,min_total)