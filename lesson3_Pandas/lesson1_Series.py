import numpy as np
import pandas as pd

# способ создания обхектов Series на основе списков
myindex = ["USA", "Canada", "Mexico"]
mydata = [1776, 1867, 1821]

# по умолчанию создает цифровой индекс (0,1,2...), который можно измнить
myser = pd.Series(data=mydata)
print(f"with default index: {myser}")

# добавляем индекс для pd.Series из myindex
myser_index = pd.Series(data=mydata, index=myindex)
print(f"with custom index: {myser_index}")
print(f"Тип данных для: {type(myser_index)}")
print(f"myser_index[0]: {myser_index[0]}")
print(f"myser_index['USA']: {myser_index['USA']}")

# Способ создания объектов на основе словарей
ages = {'Sam ':5, 'Frank':10, 'Spike':7}
series_ages = pd.Series(ages)
print(f"Series на основе словаря: \n{series_ages}")



