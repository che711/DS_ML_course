import numpy as np
import pandas as pd

data_one = {'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']}
data_two = {'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}

one = pd.DataFrame(data_one)
two = pd.DataFrame(data_two)

print(f'\n -> \n{one}')
print(f'\n -> \n{one}')

# переименование колонок для валидного объединения строк
two.columns = one.columns
print(f'\n -> \n{two}')

print(f'\npd.concat([one, two], axis=0) -> \n{pd.concat([one, two], axis=0)}')

# сохраняем предыдущий dataFrame в переменную и изменяем ему индекс
mydf = pd.concat([one,two], axis=0)
mydf.index = range(len(mydf))
print(f'\nmydf -> \n{mydf}')


# print(f'\n -> \n{}')


