import numpy as nm
import pandas as pd

df = pd.read_csv('../course_data/03-Pandas/tips.csv')
print(f"просто выводим массив: \n{df}")

# меням тип данных с числа на строку
num = 1234567890
print(f"меняем тип данных с int на str и забираем последние четыре элемента строки: \n{str(num)[0]}")


