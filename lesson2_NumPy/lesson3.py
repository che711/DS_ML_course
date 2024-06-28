import numpy as np

# создаем массив
arr = np.arange(0, 10)
print(f"Array: {arr}")

print(f"arr +5: {arr +5}")
print(f"arr -2: {arr - 2}")
print(f"arr + arr: {arr+arr}")
print(f"arr * arr: {arr*arr}")
print(f"arr / arr: {arr/arr}")
print(f"1/arr: {1/arr}")
print(f"Квадратный корень каждого элемента: {np.sqrt(arr)}")
print(f"Синус каждого элемента массива: {np.sin(arr)}")
print(f"натуральный логарифм элемента массива: {np.log(arr)}")
print(f"Сумма всех элементов массива: {np.sum(arr)}")
print(f"Среднее значение всех элементов массива: {np.mean(arr)}")
print(f"Max значение всех элементов массива: {np.max(arr)}")
print(f"Дисперсия всех элементов массива: {np.var(arr)}")
print(f"Стандартное отклонение элементов массива: {np.std(arr)}")

# создаем двумерный массив
arr2d = np.arange(0,25).reshape(5,5)
print(f"Cоздаем двумерный массив arr2d: {arr2d}")
# сумма элементов массива
print(f"Cумма элементов двумерного массива: {arr2d.sum()}")
print(f"Cумма элементов колонок -> axis=0: {arr2d.sum(axis=0)}")
print(f"Cумма элементов строк -> axis=1: {arr2d.sum(axis=1)}")




