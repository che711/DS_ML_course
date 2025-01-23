import numpy as np
import pandas as pd


# nan - мы не знаем что это за значение
print(f"\nnp.nan -> {np.nan}")

# новое обозначение для отсутствующих значений
print(f"\npd.NA -> {pd.NA}")

# NaT - not a timestamp
print(f"\npd.NaT -> {pd.NaT}")

# поскольку мы не знаем чему равно nan -> будет False
print(f"\nnp.nan == np.nan -> {np.nan == np.nan}")

# проверяем является ли значение неизвестным
print(f"\nnp.nan is np.nan -> {np.nan is np.nan}")

df = pd.read_csv('../course_data/03-Pandas/movie_scores.csv')
print(f"\n -> \n{df}")

# проверяем содержит ли dataframe отсутствующие данные
print(f"\nпроверяем содержит ли dataframe отсутствующие данные -> \n{df.isnull()}")

print(f"\ndf[(df['pre_movie_score'].isnull()) & (df['first_name'].notnull())] -> \n{df[(df['pre_movie_score'].isnull()) & (df['first_name'].notnull())]}")

# .dropna() удаляет все строки в которых есть хоят бы один NaN
print(f"\n.dropna() удаляет все строки в которых есть хоят бы один NaN -> \n{df.dropna()}")

#  Keep only the rows with at least  1 non-NA values. For example: df.dropna(thresh=1)
print(f"\nОставляем строки с одним и более значением NaN -> \n{df.dropna(thresh=1)}")

# удалить все колонки в которых есть хотя бы одно значение  NaN. B df есть вторая строка в которой все колонки равны NaN
df.dropna(axis=1)
print(f"\ndf.dropna(axis=1) -> \n{df.dropna(axis=1)}")

# удаляются все строки в которых в колонке "last_name" встречается NaN
df.dropna(subset=['last_name'])
print(f"\ndf.dropna(subset=['last_name']) -> \n{df.dropna(subset=['last_name'])}")

# print(f"\n -> \n{help(df.fillna)}")

# Заменяет NaN на НЕИЗВЕСТНО
print(f"\ndf.fillna('НЕИЗВЕСТНО') -> \n{df.fillna('НЕИЗВЕСТНО')}")

# быть внимательными с .fillna(), тк в разных колонках разные типы данных
df.info()
print('\n')
df.fillna("НЕИЗВЕСТНО").info()

# замена значений NaN в колонке на 0
print(f"\n df['pre_movie_score'].fillna(0)-> \n{df['pre_movie_score'].fillna(0)}")

# сохранение среднего значения вместо NaN:
df["pre_movie_score"].mean() # находим среднее значение
df['pre_movie_score'].fillna(df['pre_movie_score'].mean())  # передаем среднее значение вместо NaN (без сохранения)
print(f"\ndf['pre_movie_score'].fillna(df['pre_movie_score'].mean()) -> \n{df['pre_movie_score'].fillna(df['pre_movie_score'].mean())}")

# Замена NaN на интерполированные значения
# новый словарь
airline_tix = {'first': 100, "business": np.nan, 'economy_plus': 50, 'economy': 30}

# создаем новый объект Series
ser = pd.Series(airline_tix)
print(f"\n -> \n{ser}")
# линейная интерполяция. Данные должны быть упорядочены
print(f"\nser.interpolate() -> \n{ser.interpolate()}")


