#PyBank
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import csv
import os
file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
os.chdir(dir_path)

total_months = 0
net_total = 0
total_changes = 0
max_changes = 0
min_changes = 0
max_date = ''
min_date = ''
lastPrice = 0
changes =0
with open('./Resources/budget_data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    # read the file
    for row in reader:
      
        if total_months == 0:
            lastPrice = int(row[1])
        
        net_total += int(row[1])
        changes = int(row[1]) - lastPrice
        total_changes += changes
        total_months += 1
        lastPrice = int(row[1])
        
        # find max and min
        if changes >= max_changes :
            max_changes = changes
            max_date = row[0]
    
        if changes <= min_changes :
            min_changes = changes
            min_date = row[0]

avg_total = round(total_changes/(total_months-1),2)

#print to terminal
print('Financial Analysis')
print('----------------------------')
print('Total Months:',total_months)
print('Total:',net_total)
print('Average Change: $',avg_total)
print('Greatest Increase in Profits: ',max_date,max_changes)
print('Greatest Decrease in Profits: ',min_date,min_changes)

#write to file
with open('./analysis/PyBank_analysis.txt', 'w') as file:
    file.write('Financial Analysis\n')
    file.write('----------------------------\n')
    file.write('Total Months: '+ str(total_months) + '\n')
    file.write('Total: ' + str(net_total) + '\n')
    file.write('Average Change: $ '+ str(avg_total) + '\n')
    file.write('Greatest Increase in Profits: '+ str(max_date) + ' '+ str(max_changes) + '\n')
    file.write('Greatest Decrease in Profits: '+ str(min_date) + ' '+ str(min_changes) + '\n')
