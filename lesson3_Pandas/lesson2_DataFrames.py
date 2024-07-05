import numpy as np
import pandas as pd
import sys


np.random.seed(101)
mydata = np.random.randint(0, 101, (4,3))
print(f"{mydata}")

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






