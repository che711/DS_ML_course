import numpy as np

print(f"Создайте массив из 10 нулей: np.zeros(10) -> {np.zeros(10)}")
print(f"Создайте массив из 10 единиц: np.ones(10) -> {np.ones(10)}")

print(f"\nСоздайте массив из 10 пятёрок np.ones(10)+4 -> {np.ones(10)+4}")
print(f"Создайте массив из 10 пятёрок np.ones(10)*5 -> {np.ones(10)*5}")  # немного другой вариант

print(f"\nСоздайте массив целых чисел от 10 до 50 включительно: np.arange(10, 51) -> {np.arange(10,51)}")
print(f"Создайте массив всех чётных чисел от 10 до 50 включительно: np.arange(0,51,2)-> {np.arange(0,51,2)}")  # добавляется шаг 2
print(f"Создайте матрицу 3x3 со значениями от 0 до 8 включительно: np.arange(9).reshape(3,3) -> {np.arange(9).reshape(3,3)}")
print(f"Создать единичную матрицу 3х3 через np.eye(3) -> \n{np.eye(3)}")

# Генерация данных
print(f"Сгенерируйте случайное число в диапазоне от 0 до 1: np.random.rand(1) -> \n{np.random.rand(1)}")
print(f"Cгенерируйте массив из 25 случайных чисел, выбранных из стандартного нормального распределения: np.random.randn(25) -> \n{np.random.randn(25)}")
print(f"Cоздать матрицу от 0 до 1 с шагом 0,01: (np.arange(1,101)/100).reshape(10,10)    -> \n{(np.arange(1,101)/100).reshape(10,10)}")
print(f"Создайте массив из 20 равноудалённых друг от друга точек между 0 и 1: np.linspace(0,1,20) -> \n{np.linspace(0,1,20)}")

# Индексация Numpy
mat = np.arange(1,26).reshape(5,5)
print(f"Array for work: np.arange(1,26).reshape(5,5) -> \n{mat}")
print(f"Вывести число из четвертой строки и пятой колонки: mat[3,4] -> {mat[3,4]}")
print(f"Часть матрицы mat[2:,1:] -> \n{mat[2:,1:]}")
print(f"Часть матрицы mat[:3,1:2] -> \n{mat[:3,1:2]}")
print(f"Часть матрицы mat[4,] -> \n{mat[4,]}")
print(f"Часть матрицы mat[4] -> \n{mat[4]}")
print(f"Выбираем диапазон строк: mat[3:5] -> \n{mat[3:5]}")
print(f"Сумма элементов матрицы mat.sum(): -> \n{mat.sum()}")
print(f"Среднеквадратичное отклонение значений в матрице mat.std(): -> \n{mat.std()}")
print(f"Сумму каждой из колонок в матрице mat.sum(axis=0): -> \n{mat.sum(axis=0)}")

seed = (np.random.seed(101)).np.random.rand(1)
print(f"\nОдно и то же случайное число: (np.random.seed(101)).np.random.rand(1) -> {seed}")



