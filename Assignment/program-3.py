import pandas as pd
import csv

# Create a list of cricketer records
cricketers = [
    (1, 'Sachin Tendulkar', 'India', 463, 18426),
    (2, 'Ricky Ponting', 'Australia', 463, 13704),
    (3, 'Kumar Sangakkara', 'Sri Lanka', 404, 14234),
    (4, 'Brian Lara', 'West Indies', 299, 10405),
    (5, 'Virat Kohli', 'India', 254, 12745),
    (6, 'Jacques Kallis', 'South Africa', 328, 11579),
    (7, 'AB de Villiers', 'South Africa', 228, 9577),
    (8, 'MS Dhoni', 'India', 350, 10773),
    (9, 'Sanath Jayasuriya', 'Sri Lanka', 445, 13430),
    (10, 'Rohit sharma', 'India', 375, 11739),
    (11, 'Yuvraj Singh', 'India', 304, 8701),
    (12, 'Shane Warne', 'Australia', 194, 2939),
    (13, 'Muttiah Muralitharan', 'Sri Lanka', 350, 1265),
    (14, 'Glenn Maxwell', 'Australia', 250, 3843),
    (15, 'Kevin Pietersen', 'England', 251, 8181)
]

# Create a CSV file and write the records

with open("D:/sqlite3/csv/cricketers.csv", "w",newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['cid', 'cname', 'country', 'match', 'run'])  # Header
    writer.writerows(cricketers)  # Insert records

# 1.Create dataframe from csv file.

df = pd.read_csv("D:/sqlite3/csv/cricketers.csv")

# 2.Print all records.
df

# 3.Print only first 5 records.
df.head()

# 4.Print only last 5 records.
df.tail()

# 5.Print records from records number 8.
df.iloc[7]

# 6.Change index numbering. start from 100.
df.index = range(100, 100 + len(df))
df

# 7.Add New column "Average" with average value and print all records.
df['Average'] = df['run'] / df['match']
df

# 8.Print only Cname.
df['cname']

# 9.Print Cricketer Name and its Average.
df[['cname','Average']]

# 10.Change column name with "Cid, Cricketer_Name, Match, Run, Average".
df.columns = ['Cid', 'Cricketer_Name', 'Country', 'Match', 'Run', 'Average']
df

# 11.Print those record where cricker play match > 25.
df[df['Match'] > 25]

# 12.Print those record where cricker play match > 25 and country is "India".
(df[(df['Match'] > 25) & (df['Country'] == 'India')])

# 13. Print all those records whose crickert average is more than 30.
df[df['Average'] > 30]

# 14.Print only crickert name whose average > 30.
df[df['Average'] > 30]['Cricketer_Name']

# 15.Print cricket name and country whose average > 30.
df[df['Average'] > 30][['Cricketer_Name', 'Country']]

# Print player records with average. and write this data into player.csv file. Do all this task from python.
players=[
    ('cid', 'cname', 'country', 'match', 'run','average'),
    (1, 'Sachin Tendulkar', 'India', 463, 18426,39.796976),
    (2, 'Ricky Ponting', 'Australia', 463, 13704,29.598272),
    (3, 'Kumar Sangakkara', 'Sri Lanka', 404, 14234,35.232673),
    (4, 'Brian Lara', 'West Indies', 299, 10405,34.799331),
    (5, 'Virat Kohli', 'India', 254, 12745,50.177165),
    (6, 'Jacques Kallis', 'South Africa', 328, 11579,35.301829),
    (7, 'AB de Villiers', 'South Africa', 228, 9577,42.004386),
    (8, 'MS Dhoni', 'India', 350, 10773,30.780000),
    (9, 'Sanath Jayasuriya', 'Sri Lanka', 445, 13430,30.179775),
    (10, 'Rohit sharma', 'India', 375, 11739,31.304000),
    (11, 'Yuvraj Singh', 'India', 304, 8701,28.621711),
    (12, 'Shane Warne', 'Australia', 194, 2939,15.149485),
    (13, 'Muttiah Muralitharan', 'Sri Lanka', 350, 1265,3.614286),
    (14, 'Glenn Maxwell', 'Australia', 250, 3843,15.372000),
    (15, 'Kevin Pietersen', 'England', 251, 8181,32.593625)
]

with open("D:/sqlite3/csv/player.csv", "w",newline='') as f:
    writer = csv.writer(f)
    writer.writerows(players)

with open("D:/sqlite3/csv/player.csv", "r",newline='') as f:
    writer = csv.reader(f)
    
