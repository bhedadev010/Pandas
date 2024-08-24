import numpy as np
import pandas as pd

country = ['a','b','c','d']

a = pd.Series(country)
print(a)

run = [1,2,3,4,5]
run_ser = pd.Series(run)
print(run_ser)


marks = [12,43,5,6,87]
sub = ['wow','gg','nice','dec','dev']
print(pd.Series(marks,index=sub))\


marks = [12,43,5,6,87]
sub = ['wow','gg','nice','dec','dev']
print(pd.Series(marks,index=sub,name="DEV MARKS"))

marks = {
    'wow':2,
    'dec':23,
    'we':34
}
print(pd.Series(marks,name="woq MARKS"))