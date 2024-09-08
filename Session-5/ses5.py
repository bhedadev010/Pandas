import numpy as np
import pandas as pd

s = [
    [1,2,3,4,5],
    [12,13,14,15,16],
    [3,4,5,6,7],
    [5,6,7,8,9]
]

s = pd.DataFrame(s,columns=['abc','xyz','sed','dex','red'])
# print(s)


st = {
    'wow' : ['dev','ew','re'],
    'iq' : [100,2,54],
    'marks' : [43,54,76],
    'pac' : [10,2,2]
}

st = pd.DataFrame(st)
st.set_index('wow',inplace=True)
# print(st)


movies = pd.read_csv('movies.csv')
# print(movies)

ipl = pd.read_csv('ipl-matches.csv')
print(ipl)

print(movies.shape)
print(ipl.shape)

print(movies.dtypes)
print(movies.index)
print(ipl.index)

print(movies.columns)
print(ipl.columns)

print(movies.values)

print(movies.info())

print(movies.describe())

ipl.rename(columns={'City':'WOW'},inplace=True)

print(ipl.head(2))
print(ipl.tail(2))
print(ipl.sample(5))

print(ipl.isnull().sum())
print(ipl.duplicated().sum())

#rename

print(s.columns)
s.rename(columns={
    'abc':'dev',
    'sed':'omg'
},inplace=True)
print(s.columns)