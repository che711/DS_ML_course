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
# По диагонали всегда единицы, потому что переменная идеально коррелирует сама с собой
print(f"Корреляция -> \n{df.corr(numeric_only=True)}")

# считает значения в колонке
print(f"считает значения в колонке -> \n{df['sex'].value_counts()}")

# количество всех значений в колонке
print(f"LEN: {len(df['day'].unique())}")
# то же самое что и код выше
print(f" -> \n{df['day'].nunique()}")

# массив с уникальными значениями в этой колонке
print(f"массив с уникальными значениями в этой колонке -> \n{df['day'].unique()}")

# кол-во строк с уникальными значениями в колонке
print(f"кол-во строк с уникальными значениями в колонке -> \n{df['day'].value_counts()}")

# замена значения во всей колонке
print(f"замена значения во всей колонке -> \n{df['sex'].replace('Female', 'F')}")

# замена двух значений в колонке
print(f"замена двух значений в колонке -> \n{df['sex'].replace(['Female', 'Male'], ['F', 'M'])}")

# тоже самое что и .replace() только через словарь. Подходит для замены большого числа значений
mymap = {'Female': 'F', 'Male': 'M'}
df['sex'].map(mymap)
print(f"замена значений в колонке через список -> \n{df['sex'].map(mymap)}")

# показывает дупликаты строк
print(f"дупликаты -> \n{df.duplicated()}")

simple_df = pd.DataFrame([1,2,2,2],['a','b','c','d'])  # создаем простой dataFrame
print(f"показывем дупликаты в simple_df -> \n{simple_df.duplicated()}")  # показывем дупликаты

# метод для удаления дупликатов
print(f"метод для удаления дупликатов .drop_duplicates() -> \n{simple_df.drop_duplicates()}")

# находится ли значение колонки между двумя указанаыми величинами
print(f"находится ли значение колонки между двумя указанаыми величинами -> \n{df['total_bill'].between(10, 20, inclusive = 'both')}")

# фильтруем по условию выше
print(f"фильтруем по условию выше -> \n{df[df['total_bill'].between(10, 15, inclusive = 'both')]}")

# выводим десять строк с наибольшими значениями в колонке 'tip'. Фактически сортируем данные
print(f"выводим десять строк с наибольшими значениями в колонке 'tip'. Фактически сортируем данные -> \n{df.nlargest(10, 'tip')}")

# тоже что и код выше
df.sort_values('tip', ascending=False).iloc[0:5]
print(f"тоже что и код выше -> \n{df.sort_values('tip', ascending=False).iloc[0:5]}")

# выводим десять строк с наименьшими значениями в колонке 'tip'. Метод обратный .nlargest()
df.nsmallest(5, 'tip')
print(f"выводим десять строк с наименьшими значениями в колонке 'tip'. Метод обратный .nlargest() -> \n{df.nsmallest(5, 'tip')}")

# тоже что и код выше
new_df = df.sort_values('tip', ascending=True).iloc[0:5]
print(f"выводим десять строк с наименьшими значениями в колонке tip. Метод обратный .nlargest() -> \n{new_df}")

# случайные строки из dataFrame. всегда разные значения
df.sample(5)
print(f"случайные строки из dataFrame. всегда разные значения -> \n{df.sample(5)}")

# выводим одну десяту всех строк из данного dataFrame
df.sample(frac=0.1)
print(f"выводим одну десяту всех строк из данного dataFrame: df.sample(frac=0.1) -> \n{df.sample(frac=0.1)}")





