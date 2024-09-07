import numpy as np
import pandas as pd

student_data = [
    [100,80,10],
    [54,76,34],
    [123,54,67],
    [70,45,34]
]

a = pd.DataFrame(student_data,columns=['iq','marks','average'])

print(a.sum(axis=1))

print(a.mean(axis=1))

print(a.var())

#indexing
print(a['iq'])

#slicing
print(a[0:2])


#doubt
print(a.iloc[[0,2]])

ipl = pd.read_csv('ipl-matches.csv')
# a = ipl['MatchNumber'] == 'Final'
# b = ipl[a]
# print(b[['Season','WinningTeam']])
print(ipl[ipl['MatchNumber']=='Final'][['Season','WinningTeam']])