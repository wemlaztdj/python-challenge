# python-challenge
## Description
Module 3 Challenge has two Python challenges - PyBank and PyPoll.

Resources folders that contain the dataset, the CSV file.
The analysis folders contain the results file.

## PyBank
The PyBank dataset(budget_data.csv) has two columns: "Date" and "Profit/Losses".

![example](https://github.com/wemlaztdj/python-challenge/blob/main/Screenshot/budget_data.png)

The Python script will calculate:

The total number of months included in the dataset.

The total net amount of "Profit/Losses" over the entire period.

The changes in "Profit/Losses" over the entire period, and then the average of those changes.

The greatest increase in profits (date and amount) over the entire period.

The greatest decrease in profits (date and amount) over the entire period.

Print the analysis to the terminal and export the results to a text file. The results file is shown below.

![example](https://github.com/wemlaztdj/python-challenge/blob/main/Screenshot/PyBank_analysis.png)



## PyPoll

The PyPoll dataset(election_data.csv) has three columns: "Voter ID", "County", and "Candidate".

![example](https://github.com/wemlaztdj/python-challenge/blob/main/Screenshot/election_data.png)

The Python script will calculate:

The total number of votes cast.

A complete list of candidates who received votes.

The percentage of votes each candidate won.

The total number of votes each candidate won.

The winner of the election is based on the popular vote.

Print the analysis to the terminal and export the results to a text file. The results file is shown below.

![example](https://github.com/wemlaztdj/python-challenge/blob/main/Screenshot/PyPoll_analysis.png)


## Installation

Both of these scripts are using csv and os.

```python
import csv
import os
```
