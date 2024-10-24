import numpy as np
import pandas as pd
import sys


np.random.seed(101)
mydata = np.random.randint(0, 101, (4,3))
print(f"Постоянное рандомные числа: {mydata}")

myindex = ['CA','NY','AZ','TX']
mycolumns= ['Jen','Feb','Mar']

# cоздаем объект DataFrame с одним параметром data=mydata
df = pd.DataFrame(mydata)
print(f"\ndf with one parameter: data=mydata and -> \n{df}")

# cоздаем объект DataFrame с двумя параметрами data=mydata и index=myindex
df = pd.DataFrame(data=mydata, index=myindex)
print(f"\ndf with two params: data=mydata and index=myindex -> \n{df}")

# cоздаем классический DataFrame с тремя параметрами data=mydatа, index=myindex, columns=mycolumns
df = pd.DataFrame(data=mydata, index=myindex, columns=mycolumns)
print(f"\ndf with two params: data=mydata, index=myindex and columns=mycolumns-> \n{df}")

# общая информация о датафрейме +показывает кол-во памяти, занаятое на машине
print(f"\nОбщая информация о созданном dataFrame: df.info -> \n{df.info()}\n")

# читаем .csv файл из исходных данных
df = pd.read_csv('../course_data/03-Pandas/tips.csv')
print(f'Читаем .csv файл из исходных данных через pd.read_csv -> \n{df}')

# атрибут columns выдает список названий колонок. Возвращает объект Index
print(f"\nатрибут columns: df.columns -> {df.columns}\n")

# атрибут index выдает список индексов (от 0 до 244). Возвращает объект Index
print(f"\nатрибут index: df.index -> {df.index}\n")

# вывод первых строк DataFrame
print(f"Метод .head() выводит первые строки: -> {df.head()}")

# вывод последних строк DataFrame через метод .tail()
print(f"Bывод последних строк DataFrame через метод .tail() -> {df.tail(10)}")

# Вывод полной информации о DataFrame
print(f"Вывод полной информации о DataFrame: {df.info}")

# подсчет всех данных в цифровых колонках
print(f"подсчет всех данных в цифровых колонках: df.describe() -> \n{df.describe()}")

# транспонирование
print(f"Транспонирование - менять местами колонки и строки: \n{df.describe().transpose()}")

## Columns
# "Вывод колонки
print(f"Вывод колонки: df['total_bill'] -> {df['total_bill']}")

# "Вывод колонок. указываем список колонок
mycols = ['total_bill', 'tip']
print(f"\nВывод колонок. указываем список колонок -> \n{df[['total_bill', 'tip']]}")
print(f"\nВывод колонок. cоздаем новый список колонок mycols -> \n{df[mycols]}")

# создать данные для новой колонки в DataFrame
print(f"новая колонка сумма двух колонок: \n{df['tip'] + df['total_bill']}")
df['tip'] + df['total_bill']

# создать данные для новой колонки в DataFrame
print(f"Процент чаевых от суммы счета: \n{100 * df['tip'] / df['total_bill']}")
tip_percentage = 100 * df['tip'] / df['total_bill']

# добавить созданные данные в новую колонку DataFrame
df['tip_percentage'] = 100 * df['tip'] / df['total_bill']  # or ->  df['tip_percentage'] = tip_percentage
print(f"добавить созданные данные в новую колонку DataFram: просто ссылваемся на нее будто она уже есть -> \n{df['tip_percentage']}")
print(f"DataFram: \n{df}")

# округление
df['price_per_person'] =  np.round(df['total_bill'] / df['size'], 2)
print(f"добавить созданные данные в новую колонку DataFram: просто ссылваемся на нее будто она уже есть -> \n{df['tip_percentage']}")
print(f"DataFram: \n{df}")

# удаление колонок и строк через .drop()
# .drop() - не вносит изменения в df, а возвращает дргой dataframe
df.drop('tip_percentage', axis=1)
print(f"удалить колонку по названию: {df.drop('tip_percentage', axis=1)}")

# полное удаление колонок и строк через .drop(inplace=True) -> внесутся изменения в исходный dataframe
print(f"полное удаление колонок и строк через .drop(inplace=True) \n{df.drop('tip_percentage', axis=1, inplace=True)}")

# полное удаление колонок и строк через .drop(inplace=True) -> внесутся изменения в исходный dataframe
df = df.drop('sex', axis=1)
print(f"удалить колонку 'sex' по названию через новую переменную: \n{df}")

# Индексы и строки
print(f"df.index -> pandas сам пронумеровывает строки -> \n{df.index}")

# изменение индекса
print(f"изменение индекса -> \n{df.set_index('Payment ID')}")

# сбросить индекс
print(f"сбросить индекс через df.reset_index():  \n{df.reset_index}")

df = df.set_index('Payment ID')
print(f"устанавливаем индекс снова на колонку 'Payment ID' -> \n{df}")

# получение одной строки на основе числового индекса .iloc[] - integer based location
print(f"получение одной строки на основе числового индекса df.iloc[] -> \n{df.iloc[0]}")

# получение одной строки на основе именнованного индекса .loc[]
print(f'получение одной строки на основе именнованного индекса .loc[] => \n{df.loc["Sun5260"]}')

# получение диапазона строк .iloc[47:50]
print(f'получение диапазона строк: df.iloc[47:50]] => \n{df.iloc[47:50]}')

# получение диапазона строк .loc['Sun4608','Sun2251','Sun9774']
print(f"получение одной строки на основе именнованного индекса .loc['Sun4608','Sun2251','Sun9774'] => \n{df.loc[['Sun4608','Sun2251','Sun9774']]}")

# удаление строк по именнованному индексу только через .drop()
print(f"удаление строк по именованному индексу -> \n{df.drop('Sun2959', axis=0)}")

# удаить строки через числовой индекс нельзя. можно только сохранить новый диапазон всех строк в новый dataframe без
print(f"удаление строк через числовой индекс нельзя. можно только сохранить новый диапазон всех строк в новый dataframe без -> \n{df.iloc[0:4]}")

# новая строка должна соответствовать по количесву колонок всему dataframe
one_row = df.iloc[0]
print(f'создание новой строки: \n{one_row}')

# добавление новой строки через .concat
pd.concat([df, pd.DataFrame([one_row])], axis=0)
print(df)


