import numpy as np

mylist = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"The type of data my_list: {type(mylist)}")

myarr = np.array(mylist)
print(f"myarr: {myarr}")

# одномерный массив

myarr = np.array(mylist)
print(f"Просто переменная marr: {myarr}.\nТип данных myarr: {type(myarr)}")
print("\n")

# двумерный массив
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]  # простой вложенный список python
print(f"np.array(my_matrix): {np.array(my_matrix)},"
      f"\nтип данных np.array(my_matrix): {type(np.array(my_matrix))}")

# верхняя граница np.arange не включается в вывод
print(f"\nnp.arange(0,100,20): {np.arange(0,100,20)}")

# создавать массивы из нулей и единиц
print(f"одномерный массив из нулей: \n{np.zeros(5)}") # одномерный массив из нулей (по умолчанию numpy возвращает нули с плавающей точкой)
print(f"двумерный массив из нулей: \n{np.zeros((5,5))}")  # двумерный массив из нулей. передается кортеж, первое число кортежа - кол-во строк, воторое число кортежа - кол-во столбцов
print(f"одномерный массив из единиц: \n{np.ones(5)}") # одномерный массив из единиц (по умолчанию numpy возвращает числа с плавающей точкой)
print(f"двумерный массив из единиц: \n{np.ones((4,2))}")  # двумерный массив из единиц. передается кортеж, первое число кортежа - кол-во строк, воторое число кортежа - кол-во столбцов

# верхняя граница np.linspace в отличие от np.arange включена в вывод
print(f"np.linspace шаг 3: {np.linspace(0,10,3)} \nДлина (len(np.linspace(0,10,3)): {len(np.linspace(0,10,3))}")
print(f"np.linspace шаг 11: {np.linspace(0,10,11)} \nДлина (len(np.linspace(0,10,11)): {len(np.linspace(0,10,11))}")
print(f"np.linspace шаг 21: {np.linspace(0,10,21)} \nДлина (len(np.linspace(0,10,21)): {len(np.linspace(0,10,21))}")

# единичная матрица, на главной диагонали которой единицы,во всех остальных - нули
print(f"np.eye(5): {np.eye(5)} \nДлина np.eye(5): {len(np.eye(5))}")

# Рандомные значения
print(f"Одно рандомное значение в диапазоне от 0 до 1 с np.random.rand(1): \n{np.random.rand(1)}")
print(f"Двумерный массив из рандомных значенй от 0 до 1 с пятью строками и шестью столбцами при помощи np.random.rand(5, 6): \n{np.random.rand(5,6)}")
print(f"Двумерный массив из рандомных значений от 0 до 1 с пятью строками и двумя столбцами при помощи np.random.rand(5, 2): \n{np.random.rand(5,2)}")

# нормальное распределение (распределение Гаусса):
# Cтандартное нормальное распределение в котором математическое ожидание равно нулю, а дисперcия равно 1
print(f"Pраспределение Гаусса: {np.random.randn(10)} ")
print(f"Pраспределение Гаусса: {np.random.randn(2,3)} ")

# целые случайные числа
print(f"целые случайные числа от 2 до 101 (не включая 101), size=5: \n{np.random.randint(2, high=101, size=5)}")
print(f"целые случайные числа от 2 до 101 (не включая верзнюю границу), size=(4,5): {np.random.randint(2, high=101, size=(4,5))}")

# воспроизводимый набор случайных числе с помощью seed
seed = np.random.seed(42)
print(f"np.random.seed: {seed}")
print(f"Seed from np.random.rand(4): \n{np.random.rand(2)}")

# мы не можем указать (5, 4) потому что не 25 значений из arr не поместятся в матрицу (5,4)
arr = np.arange(0,25)
print(f"arr = np.arange(0,25): {arr},\narr.reshape(5,5): {arr.reshape(5, 5)}")

# атрибуты и методы для обработки min/max значений массива
ranarr = np.random.randint(0,102,10)
print(f"ranarr: {np.random.randint(0,102,10)}")
print(f"ranarr.max(): {np.random.randint(0,102,10).max()}")
print(f"ranarr.min(): {ranarr.min()}")
print(f"позиция max значения: {ranarr.argmax()}")
print(f"позиция min значения: {ranarr.argmin()}")


