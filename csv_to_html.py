import pandas as pd

# Read the csv file in
df = pd.read_csv('Resources/cities.csv')

# Save to file
df.to_html('Resources/myTable.htm')

# Assign to string
htmTable = df.to_html()