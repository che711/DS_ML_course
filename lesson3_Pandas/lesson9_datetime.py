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

timeser = pd.to_datetime(myser, format='mixed')
print(f'\n -> \n{timeser}')

print(f'\ntimeser[0].year -> {timeser[0].year}')

obvi_euro_date = '31-12-2000'
pd.to_datetime(obvi_euro_date, format='mixed')
print(f'\nobvi_euro_date -> {pd.to_datetime(obvi_euro_date, format='mixed')}')

euro_date = '10-12-2000'
print(f'\n -> \n{pd.to_datetime(euro_date, dayfirst=True, format='mixed')}')

styledate = '22--Dec--2000'
print(f'\n -> \n{styledate}')
# форматирование даты
print(f'\nstyledate -> {pd.to_datetime(styledate, format='%d--%b--%Y')}')

custom_date = '12th of Dec 2000'
print(f'\n -> \n{pd.to_datetime(custom_date)}')

sales = pd.read_csv('../course_data/03-Pandas/RetailSales_BeerWineLiquor.csv')
print(f'\nsalws -> \n{sales}')

sales['DATE'] = pd.to_datetime(sales['DATE'])
print(f'\n -> \n{sales['DATE']}')
print(f'\n -> \n{sales['DATE'][0].year}')

sales = pd.read_csv('../course_data/03-Pandas/RetailSales_BeerWineLiquor.csv', parse_dates = [0])
print(f'\n -> \n{sales}')
print(f'\n -> \n{sales["DATE"]}')
print(f'\n -> \n{sales['DATE'][0].year}')


sales = pd.read_csv('../course_data/03-Pandas/RetailSales_BeerWineLiquor.csv', parse_dates = [0])
print(f'\n -> \n{sales}')
sales = sales.set_index('DATE')
print(f'\n -> \n{ sales.resample(rule='YE').mean()}')

sales = pd.read_csv('../course_data/03-Pandas/RetailSales_BeerWineLiquor.csv', parse_dates = [0])


# print(f'\n -> \n{}')



# print(f'\n -> \n{}')

import os
print(f"{os.getcwd()}")
