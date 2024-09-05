import numpy as np
import pandas as pd

movies = pd.read_csv('movies.csv')
movies = movies.squeeze()
subs = pd.read_csv('subs.csv')
subs = subs.squeeze()
temp = pd.Series([1,1,2,2,3,3,4,4])
print(temp)

print(temp.drop_duplicates())
print(temp.drop_duplicates(keep='last'))
#will keep the last number in the duplicates

print(temp.duplicated().sum())


temp = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])
print(temp)
print(temp.size)  #returns 10 as there are 10 elements
print(temp.count())  #returns 7 as only values are there

print(temp.isnull().sum())

print(temp.dropna())

print(temp.fillna(temp.mean()))

print(temp[(temp == 5.0) | (temp == 99)])
print(temp[temp.isin([5.0,99])])

# print(movies.apply(lambda x:x.split()[0].upper()))

print(subs.apply(lambda x:'good day' if x > subs.mean() else 'bad day'))

