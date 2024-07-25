import numpy as np
import pandas as pd


# nan - мы не знаем что это за значение
print(f"np.nan -> {np.nan}")

# новое обозначение для отсутствующих значений
print(f"pd.NA -> {pd.NA}")

# NaT - not a timestamp
print(f"pd.NaT -> {pd.NaT}")

# поскольку мы не знаем чему равно nan -> будет False
print(f"np.nan == np.nan -> {np.nan == np.nan}")

# проверяем является ли значение неизвестным
print(f"np.nan is np.nan -> {np.nan is np.nan}")

df = pd.read_csv('../course_data/03-Pandas/movie_scores.csv')
print(f" -> \n{df}")

# проверяем содержит ли dataframe отсутствующие данные
print(f"проверяем содержит ли dataframe отсутствующие данные -> \n{df.isnull()}")


# print(f" -> \n{}")
