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
