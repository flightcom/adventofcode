import numpy as np


def get_power_level(x: int, y: int, serial_number: int) -> int:
    # print(x, y, serial_number)
    rack_id = x+10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = int(str(power_level)[-3:-2])
    power_level -= 5
    # print(power_level)
    return power_level


# test = get_power_level(3, 5, 8)
# test = get_power_level(122, 79, 57)
# test = get_power_level(217, 196, 39)
# test = get_power_level(101, 153, 71)

# print(test)

liste = []
liste = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

liste = liste.reshape(3, 3)
# array = np.array([10, 20, 30], [40, 50, 60], [70, 80, 90])

# print(liste[0][1])
print(liste)

for index, item in np.ndenumerate(liste):
    index_inc = tuple(i+1 for i in index)
    liste[index] = get_power_level(*index_inc, 3)

print(liste)

# num = 3400
# print(int(str(num)[-3:-2]))

# test = (0, 0)
# print(test+1)

78, 27

28, 79

82, 235
235, 82


width: 6, stride: 3, padding: 1 -> 4
width: 6, stride: 2, padding: 2 -> 3
width: 6, stride: 1, padding: 1 -> 6
width: 6, stride: 4, padding: 2 -> 2
width: 6, stride: 6, padding: ? -> 1
width: 6, stride: 5, padding: 1 -> 2
width: 6, stride: 5, padding: 2 -> 1

width: 300, stride: 3, padding: 1 -> 2


width / padding

int((width - stride) / padding) + 1 = W
