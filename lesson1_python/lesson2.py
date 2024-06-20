a = 1
b = 2

print(f"Value of a > b: {a > b}")

print(f'Value of "f" == "f": {"f" == "f"}')

print(f"Value of (1 == 3)or('a'=='a'): {(1 == 3) or ('a '== 'a')}")


if 1 == 2:
    print("Done")
elif 3 == 3:
    print("The second condition")
else:
    print("Not done")

seq = [1, 2, 3, 4, 5]
print(f"seq: {seq}")
for item in seq:
    print(f"just one item from seq: {item}")
for item in seq:
    print(f"just one item+1 from seq: {item+1}")
for item in seq:
    print(f"just one item+item from seq: {item+item}")

i = 1
while i < 5:
    print(f'i equal {i}')
    i = i+1
