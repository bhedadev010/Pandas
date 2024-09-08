import pandas as pd

ipl = pd.read_csv('ipl-matches.csv')
movies = pd.read_csv('movies.csv')


# # how many super over finishes have occured
#
# print(ipl[ipl['SuperOver']=='Y'])
# print(ipl[ipl['SuperOver']=='Y'].shape)
#
# #how many matches has csk won in kolkata
#
# a=ipl['WinningTeam']=='Chennai Super Kings'
# a = ipl[a]
# b=a['City']=='Kolkata'
# print(a[b])
#
# #toss winner is match winner in percentage
#
# a = ipl['TossWinner'] == ipl['WinningTeam']
# c = len(ipl[a])
# b = len(ipl)
# print((c/b)*100)

# #movies with rating higher than 8 and votes>10000
#
# a = movies[movies['imdb_rating'] > 8.0]
# b = a['imdb_votes'] > 10000
# print(a[b])

#action movies with rating greater than 7.5

b = movies[movies['genres']=='Action']
a = b['imdb_rating']>7.5

print(b[a])