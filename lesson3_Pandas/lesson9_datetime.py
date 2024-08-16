import numpy as np
import pandas as pd

from datetime import datetime


myyear = 2015
mymonth = 1
myday = 1
myhour = 2
mymin = 30
mysec = 15

mydate = datetime(myyear, mymonth, myday)
print(f'\nmydate -> {mydate}')

mydatetime = datetime(myyear, mymonth, myday, myhour, mymin, mysec)
print(f'\nmydatetime -> {mydatetime}')
print(f'\nmydatetime.year -> {mydatetime.year}')

myser = pd.Series(['Nov 3, 1990','2000-01-01', None])
print(f'\nmyser -> {myser}')





# print(f'\n -> \n{}')
# print(f'\n -> \n{}')
# print(f'\n -> \n{}')
# print(f'\n -> \n{}')
# print(f'\n -> \n{}')
# print(f'\n -> \n{}')





