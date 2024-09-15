import numpy as np
import pandas as pd

match = pd.read_csv('ipl-matches.csv')
print((match['Team1'].value_counts()+match['Team2'].value_counts()).sort_values(ascending=False))

a = pd.Series([1,1,1,2,3,2,4,3,3,22])
print(a.value_counts())

marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [80,70,14],
    [120,100,14],
    [80,70,14]
],columns=['iq','marks','package'])
print(marks)

print(marks.value_counts())

print(match[~match['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts().head())

print(match['TossDecision'].value_counts().plot(kind='pie'))     #plot not visually available in .py

