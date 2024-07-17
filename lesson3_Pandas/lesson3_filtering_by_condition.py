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

# AND -> &
# OR -> |
print(f"condition AND: \n{1 == 1 and 2 != 3}")

# если надо два и более условия использовать  & and |
print(f"выборка по двум обязательным условиям total_bill и sex через &: -> \n{df[(df['total_bill'] > 30) & (df['sex'] == 'Male')]}")
print(f"выборка по трем необязательным условиям day через | : -> \n{df[(df['day'] == 'Sun') | (df['day'] == 'Sat') | (df['day'] == 'Fri')]}")

# предыдущая строка только проще через метод .isin()
options = ['Sat','Sun']
print(f"проверка наличия слова в словаре: \n{'Sat' in options}")
print(f"использование isin(): \n{df['day'].isin(options)}")






