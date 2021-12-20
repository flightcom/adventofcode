# IMPORTS
from os import path
from scipy import stats
import math
import numpy as np
import pprint
import re
# import matplotlib.pyplot as plt
from numpy import unravel_index
import turtle
import random
import sys

np.set_printoptions(threshold=sys.maxsize)
np.core.arrayprint._line_width = 200
np.set_printoptions(edgeitems=100, linewidth=200, 
    formatter=dict(float=lambda x: "%.3g" % x))

# SETUP
input_file = path.splitext(path.basename(__file__))[0] + '.txt'
if not path.isfile(input_file):
    input_file = path.splitext(path.basename(__file__))[0].split('.')[0] + '.txt'
# input_file = path.splitext(path.basename(__file__))[0] + '.test.txt'
# input_file = 'test.txt'
if not path.isfile(input_file):
    input_file = '1.txt'

input_data = np.loadtxt(input_file, dtype=np.int64)
# with open(input_file) as f:
#     input_data = f.read()
# with open(input_file) as f:
#     input_data = f.read().split()
# with open(input_file) as f:
#     input_data = f.read().splitlines()

# if not input_data:
#     raise Exception('No content !')

# GLOBAL VARIABLES
result = 0
count = 0

def ppprint(message, file=None):
    # np.set_printoptions(threshold=np.nan)
    pp = pprint.PrettyPrinter(indent=4, stream=file, width=150)
    pp.pprint(message)


def draw(X, Y):
    plt.plot(X, Y, 'ro')
    # Reverse Y-Axis
    plt.gca().invert_yaxis()
    plt.show()

# SOLUTION GOES HERE

def format_result():
    global result
    result = [b''.join(result[:,x]) for x in range(result.shape[1])]


def possible_locations_around(position):
    global input_data
    positions = []
    (x, y) = position
    positions_to_test = [
        (x, y+1),
        (x, y-1),
        (x+1, y),
        (x-1, y),
    ]

    for p in positions_to_test:
        if input_data[p] == 1:
            positions.append(p)
    return positions

def oxygen_around(positions):
    global input_data, count
    ps = []
    for p in positions:
        p_next = possible_locations_around(p)
        for p2 in p_next:
            ps.append(p2)
            input_data[p2] = 6
    return ps

def main():
    global input_data, result, count

    starts = np.where(input_data == 2)
    start = (starts[0][0], starts[1][0])
    positions = [start]

    go = True
    while go:
        new_positions = oxygen_around(positions)
        wh = np.where(input_data == 1)
        indices = zip(*(np.where(input_data == 1) or np.where(input_data == 9)))
        lindices = list(indices)
        if len(lindices) == 0:
            go = False
        positions = new_positions
        print(len(lindices), new_positions)
        count += 1

    print('count', count)


if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)


# 371 too low