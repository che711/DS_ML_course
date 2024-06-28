import numpy as np


arr = np.arange(0, 11)
print(f"Array from 0 to 11 ->K {arr}")
print(f"Position 8 from the list above -> {arr[8]}")
print(f"Range from 3 to 7 in the list above -> {arr[3:7]}")
print(f"Range :5 -> {arr[:5]}")
print(f"Range 7: -> {arr[7:]}")

# присвоить выбранному диапазонy другое значение
arr[0:4] = 100
print(f"Update first five positions (0:4) in the list above arr[0:4] = 100: {arr}")

arr = np.arange(0,11)
print(f"\nСоздаем новый список через np.arrange(0,11) -> {arr}")

# создаются НЕ копии массива arr, а ссылки на исходный массив
slice_of_array = arr[0:5]
print(f"\nПрисваиваем новому списку значения из списка выше через slice_of_array = arr[0:5] (НЕ копии, а ссылки на элементы исходного массива) -> {slice_of_array}")

# меняем значения в списке (переписываем исходные элементы в первоначальном массиве)
slice_of_array[:5] = 99
print(f"\nМеняем значения в списке (переписываем исходные элементы в первоначальном массиве) slice_of_array[:5] = 99 -> {slice_of_array}")

# что бы не менять первоначальный массив, надо создать его копию
new_arr = np.arange(0,10)
new_arr_copy = new_arr.copy()
print(f"\nСоздаем копию первоначального массива через new_arr_copy = new_arr.copy() -> {new_arr_copy}")

# еще одна копия
slice_of_new_arr_copy = new_arr.copy()
print(f"\nСоздаем еще одну копию первоначального массива slice_of_new_arr_copy = new_arr.copy() -> {slice_of_new_arr_copy}")

# присваиваем элементам копии новые значения
slice_of_new_arr_copy[:] = 87
print(f"\nПрисваиваем элементам копии новые значения slice_of_new_arr_copy[:] = 87 -> {slice_of_new_arr_copy}")

# Работа с двумерными массивами
# создаем двумерный массив
arr_2d = np.array([[5,10,15],[20,25,30],[30,35,40]])
print(f"\nСоздaем двумерный массив -> {arr_2d}")

# в ответе первое число - кол-во строк, второе - кол-во столбцов
arr_2d.shape

# получить первую строку двумерного массива (матрицы)
arr_2d[0]

# получить тертью (последнюю) строку двумерного массива (матрицы)
arr_2d[2]

# получить второй элемент первой строки массива (матрицы)
arr_2d[0][1] # arr_2d[1,1]

# тоже самое что и выше
arr_2d[0,1]

# slices
arr_2d[:2]

# slices
arr_2d[:2,1:]

# new arr
arr = np.arange(1,11)
arr

arr > 4

bool_arr = arr >4
bool_arr

# это фактически условие для фильтрации элементров массива по "элемент > 4"
arr[bool_arr]

# тоже что и выше
new_arr[arr > 4]