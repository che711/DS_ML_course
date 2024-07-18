import numpy as nm
import pandas as pd


df = pd.read_csv('../course_data/03-Pandas/tips.csv')
# print(f"просто выводим массив: \n{df}")

# меням тип данных с числа на строку
num = 1234567890
print(f"меняем тип данных с int на str и забираем последние четыре элемента строки: \n{str(num)[-4:]}")

def last_four(num: str) -> int:
    """TBD"""
    return str(num)[-4:]
print(f"just for example using the function: \n{last_four('12341234124')}")
# следить за типом данных, передаваемых в функции !!

# применям функцию ко всему dataframe через .apply()
print(f"применям функцию ко всему dataframe через df['CC Number'].apply(last_four) -> \n{df['CC Number'].apply(last_four)}")

# добавляем новую колонку в df
df['last_four'] = df['CC Number'].apply(last_four)
print(f"dataframe с новой колонкой last_four: -> \n{df}")

print(f"выводим среднее значение .mean() -> \n{df['total_bill'].mean()}")

def yelp(price: int) -> int:
    '''TBD'''
    if price < 10: return '$'
    elif price >= 10: return '$$'
    else: return '$$$'

# добавляем еще одну колонку в существующий dataframe
df['yelp'] = df['total_bill'].apply(yelp)
print(f"выводим новую колонку df['yelp'] -> \n{df['yelp']}")




