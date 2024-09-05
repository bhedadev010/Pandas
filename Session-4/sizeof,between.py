import numpy as np
import pandas as pd
import sys

vk = pd.read_csv('kohli_ipl.csv',index_col='match_no')
vk = vk.squeeze()

movies = pd.read_csv('bollywood.csv',index_col='movie')
movies = movies.squeeze()
print(movies)

print(sys.getsizeof(movies))

print(vk[vk.between(21,99)].size)

print(vk.clip(10,200))