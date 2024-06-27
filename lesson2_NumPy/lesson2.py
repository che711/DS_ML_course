import numpy as np


arr = np.arange(0, 11)
print(f"Array from 0 to 11: {arr}")
print(f"Position 8 from the list above: {arr[8]}")
print(f"Range from 3 to 7 in the list above: {arr[3:7]}")
print(f"Range :5 -> {arr[:5]}")
print(f"Range 7: -> {arr[7:]}")

# присвоить выбранному диапазонy другое значение
arr[0:4] = 100
print(f"Update first five positions (0:4) in the list above arr[0:4] = 100: {arr}")
