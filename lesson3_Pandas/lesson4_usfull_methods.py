import numpy as np
import pandas as pd
import timeit

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

# создаем новую колонку с объектом Series с результотм применения функции к двум колонкам
df['quality'] = df[['total_bill','tip']].apply(lambda df: quality(df['total_bill'], df['tip']), axis=1)

print(f"Check both columns: \n{df['quality']}")
print(f"Full dataFrame: \n{df}")

# тоже самое что и .apply(), только быстрее, .vectoryze() нужен для того что преобразовать ф-ции, которые не предназначены для работы с numpy
df['quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])
print(f"{df.head()}")

#  этот фрагмент кода будет запускаться только один раз
setup = '''
import numpy as np
import pandas as pd
df = pd.read_csv('../course_data/03-Pandas/tips.csv')
def quality(total_bill,tip):
    if tip/total_bill  > 0.25:
        return "Generous"
    else:
        return "Other"
'''
# это фрагменты кода, для которых будет измеряться время выполнения
# (они будут выполняться много раз)
stmt_one = ''' 
df['Tip Quality'] = df[['total_bill','tip']].apply(lambda df: quality(df['total_bill'],df['tip']),axis=1)
'''

stmt_two = '''
df['Tip Quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])
'''

stmt_one = timeit.timeit(setup = setup, stmt = stmt_one, number = 1000)
stmt_two = timeit.timeit(setup = setup, stmt = stmt_two, number = 1000)
print(f"Время выполнения .apply() -> {stmt_one}")
print(f"Время выполнения.vectorize() -> {stmt_two}")
print(f"Во сколько раз .vectorize() быстрее чем .apply() -> {stmt_one/stmt_two}")

# выводит основные характеристики числовых колонок
print(f"\nСреднее значение цифровых колонок dataFrame{df.describe()}")

# меняет местами колонки и строки
print(f"меняет местами колонки и строки df.describe().transpose() -> \n{df.describe().transpose()}")

# сортировка dataFrame. параметр ascending=False - в обратном порядке
print(f"{df.sort_values(['tip', 'size'], ascending=False)}")

# вывести индекс с максимальным значением в колонке
print(f" вывести индекс с максимальным значением в колонке -> \n{df['total_bill'].idxmax()}")

# данные о строке
print(f"данные о строке 170 -> \n{df.iloc[170]}")

# Корреляция - это статистическая мера, которая показывает, насколько сильно две переменные связаны между собой. Если объяснять простыми словами, то корреляция говорит нам, как одна вещь меняется по отношению к другой.
print(f"Корреляция -> \n{df.corr(numeric_only=True)}")




