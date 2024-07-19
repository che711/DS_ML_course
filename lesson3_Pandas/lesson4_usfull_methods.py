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

# def simple(num:int)->int: return num*2 это тоже самое что и -> lambda num: num*2
lambda bill: bill*2

# example
def simple(num:int)->int: return num*2
print(simple(3))

# df['total_bill'].apply(simple) == df['total_bill'].apply(lambda num: num*2)
simple_and_lambda = df['total_bill'].apply(lambda num: num*2)
print(simple_and_lambda)

# Mетод .apply() с несколькими колонками
# проще называеть аргументы функции так же как и колонки dataframe
def quality(total_bill:float, tip:float) -> float:
    if tip/total_bill > 0.25: return 'Great tips'
    else: return 'Normal tips'
print(f"{quality(16.99, 1.01)}")















