import numpy as nm
import pandas as pd

df = pd.read_csv('../course_data/03-Pandas/tips.csv')
print(df)

# выбираем строки в колонке по условию
bills_more_than_40 = df['total_bill'] >= 40
print(bills_more_than_40)

# Выбираем мужчин из таблицы
men = df['sex'] != 'Female'
print(f'Выбираем мужчин из таблицы: \n{men}')

print(df[df['sex'] != 'Female'])

# Выбираем строки с воскресеньем
sunday = [df['day'] == 'Sun']
print(f"выбираем воскресенье: \n{sunday}")






