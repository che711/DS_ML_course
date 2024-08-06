import numpy as nm
import pandas as pd

df = pd.read_csv('../course_data/03-Pandas/mpg.csv')
print(f"\n -> \n{df}")

# находим все ункальные значения в колонке
df['model_year'].unique()
print(f"\n -> \n{df['model_year'].unique()}")
# находим все ункальные значения в колонке
df['cylinders'].value_counts()

# groupby возвращает ленивый объект, который ожидает когда к нему обратятся
print(f"\n -> \n{df.groupby('model_year')}")



# model_year стал индексом и для каждого значения сгруппировали среднее значение для каждой из числовых колонок
# т.е. получили dataframe c индексом model_year
df.groupby('model_year').mean(numeric_only=True)
print(f"\n -> \n{df.groupby('model_year').mean(numeric_only=True)}")

# мультииндекс
df.groupby(['model_year', 'cylinders']).mean(numeric_only=True)
print(f"\n -> \n{df.groupby(['model_year', 'cylinders']).mean(numeric_only=True)}")

# мультииндекс
print(f"\n -> \n{df.groupby(['model_year', 'cylinders']).mean(numeric_only=True)['mpg']}")

# основные данные
print(f"\n -> \n{df.groupby('model_year').describe()}")

# создаем новый dataFrame
year_cyl = df.groupby(['model_year', 'cylinders']).mean(numeric_only=True)
print(f"\n -> \n{year_cyl}")

# узнаем как называются отдельные составляющией индекса
print(f"\n -> \n{year_cyl.index.names}")

# узнаем как называются все года и цилиндры
print(f"\n -> \n{year_cyl.index.levels}")

# данные за два года
print(f"\n -> \n{year_cyl.loc[[70, 79]]}")

# данные только за один год
print(f"\n -> \n{year_cyl.loc[70]}")

# Персечение или crosssection
# метод xs() принимает только одно значение для key, т.к. не работает со списками
print(f"\n -> \n{year_cyl.xs(key=70, level='model_year')}")

# есть смысл сохранять данный в переменные с понятным названием, что это за dataframe
for_cylinders = year_cyl.xs(key=4, level='cylinders')
print(f"\n -> \n{for_cylinders}")

# даные только с выбранными значениями цилиндров
print(f"\n -> \n{df[df['cylinders'].isin([6,8])].groupby(['model_year', 'cylinders']).mean(numeric_only=True)}")

# поменять местами внешинй уровень (model_year) и внутренний уровень (cylinders) местами -> .swaplevel()
print(f"\n -> \n{year_cyl.swaplevel()}")

# изменение сортировки
print(f"\n -> \n{year_cyl.sort_index(level='model_year', ascending=False)}")

# агрегация данных
print(f"\n -> \n{df.agg({'mpg':["max", "mean"], 'weight': ['mean', 'std']})}")

# разобраться почему не работает
# print(f"\n -> \n{df.agg(['std', 'mean']).mean()['mpg']}")


















