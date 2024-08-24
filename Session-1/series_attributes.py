import numpy as np
import pandas as pd

country = ['a','b','c','d','a','b']
w = {
    'w':2,
    't':4,
    'y':5,
    'u':5,
    'i':2
}
w = pd.Series(w,name="gg")
a = pd.Series(country,name="wow dev")
print(a)
print(w)

#.size
print("size of a :",a.size)
print("size of w :",w.size)

#.dtype
print("dtpe of a:",a.dtype)
print("dtypr of w :",w.dtype)

#.drop_dulplicates
print("drop_dupli of a : ",a.drop_duplicates())
print("drop_dupli of w : ",w.drop_duplicates())

#unique
print("unique of a :",a.unique())
print("unique of w :",w.unique())

#Index.is_unique()
print("index unique A :",a.index.is_unique())
print("index unique w :",w.index.is_unique())

#is_unique
print("index unique A :",a.is_unique)
print("is index w :",w.is_unique)

##index  (will be different for normal index and provided index)
print("index a :",a.index)
print("index w :",w.index)

#values (index can be also provided)(slicing can also be performed)


# subs = pd.read_csv('subs.csv')  [this is used to read data from file present in same folder or other]
# subs.squeeze()    [this is used to convert datta from dataframe mode to normal form]

#by default loads as dataframe type and using sqquze canbe converted.

