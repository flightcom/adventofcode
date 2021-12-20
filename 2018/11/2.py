# IMPORTS
from os import path
from scipy import stats
import numpy as np
import pprint
import re
import matplotlib.pyplot as plt
from numpy import unravel_index

# SETUP
input_file = path.splitext(path.basename(__file__))[0] + '.txt'
if not path.isfile(input_file):
    input_file = '1.txt'

# with open(input_file) as f:
#     input_data = f.read().split()
with open(input_file) as f:
    input_data = f.read().splitlines()


if not input_data:
    raise Exception('No content !')


result = None

# FUNCTIONS


def ppprint(message, file=None):
    np.set_printoptions(threshold=np.nan)
    pp = pprint.PrettyPrinter(indent=4, stream=file)
    pp.pprint(message)


def draw(X, Y):
    plt.plot(X, Y, 'ro')
    # Reverse Y-Axis
    plt.gca().invert_yaxis()
    plt.show()

# SOLUTION GOES HERE


def get_cell_power_level(x: int, y: int, serial_number: int) -> int:
    rack_id = x+10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = int(str(power_level)[-3:-2])
    power_level -= 5
    return power_level


def fill_grid(grid):
    for index, item in np.ndenumerate(grid):
        index_inc = tuple(i+1 for i in index)
        grid[index] = get_cell_power_level(*index_inc, input_data)


def grid_pooling(grid, stride: int, padding: int):
    shape = grid.shape
    new_grid_width = int((shape[0] - stride) / padding) + 1
    new_grid_height = int((shape[1] - stride) / padding) + 1
    new_grid = np.zeros((new_grid_width, new_grid_height))
    for i in range(0, new_grid_width):
        for j in range(0, new_grid_height):
            x_start = i*padding
            x_end = i*padding + stride
            y_start = j*padding
            y_end = j*padding + stride
            new_grid[i, j] = grid[x_start:x_end, y_start:y_end].sum()
    return new_grid


def main():
    global input_data, result

    input_data = int(input_data[0])
    padding = 1
    grid = np.zeros((300, 300))
    fill_grid(grid)

    maximum = 0
    maximum_coords = None
    maximum_size = 0

    for i in range(1, 301):
        stride = i
        grid_reduced = grid_pooling(grid, stride, padding)
        max_value = grid_reduced.max()
        if max_value > maximum:
            maximum = max_value
            maximum_coords = unravel_index(
                grid_reduced.argmax(), grid_reduced.shape)
            maximum_size = i

    result = (*tuple([(n+1) for n in maximum_coords]), maximum_size)


if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
    # with open('out.txt', 'w') as f:
    #     ppprint(result, file=f)
