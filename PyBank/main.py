#PyBank
#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import pandas as pd

df = pd.read_csv('PyBank/Resources/budget_data.csv')

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


with open('PyBank/analysis/PyBank_analysis.txt', 'w') as file:
    file.write('Financial Analysis\n')
    file.write('----------------------------\n')
    file.write('Total Months: {}'.format(total_months) + '\n')
    file.write('Total: {}' .format(net_total) + '\n')
    file.write('Average Change: $ {}' .format(avg_total) + '\n')
    file.write('Greatest Increase in Profits: {}'.format(max_date) + ' {}'.format(max_total) + '\n')
    file.write('Greatest Decrease in Profits: {}'.format(min_date) + ' {}'.format(min_total) + '\n')
