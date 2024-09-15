import numpy as np
import pandas as pd

a = pd.Series([1,1,1,2,2,3])

# will return a table which contains the number of times the specific thing is repeated
print(a.value_counts())

ipl = pd.read_csv('ipl-matches.csv')

# find which player has won most potm -> in finals and qualifiers

print(ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts().head())

#matches each team played

print((ipl['Team1'].value_counts()+ipl['Team2'].value_counts()).sort_values(ascending=False))

students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)

#we can also select multiple columns in by parameter and multiple in ascending but it is not useful
print(students.sort_values('name',na_position='first',inplace=True,ascending=True))

