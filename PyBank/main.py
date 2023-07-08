#PyBank

import pandas as pd

df = pd.read_csv('python-challenge/PyBank/Resources/budget_data.csv')
total_months = df['Date'].count()
print (total_months)