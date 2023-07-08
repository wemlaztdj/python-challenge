#PyBank

import pandas as pd

df = pd.read_csv('budget_data.csv')
total_months = df['Date'].count()
total_months