# IMPORTS
from os import path
from scipy import stats
import math
import numpy as np
import pprint
import re
# import matplotlib.pyplot as plt
from numpy import unravel_index
import sys, getopt
import operator

# SETUP
input_file = path.splitext(path.basename(__file__))[0] + '.txt'
# input_file = 'test.txt'
if not path.isfile(input_file):
    input_file = '1.txt'

# with open(input_file) as f:
#     input_data = f.read()
# with open(input_file) as f:
#     input_data = f.read().split()
with open(input_file) as f:
    input_data = f.read().splitlines()


if not input_data:
    raise Exception('No content !')

result = 0

# FUNCTIONS
def ppprint(message, file=None):
    # np.set_printoptions(threshold=np.nan)
    pp = pprint.PrettyPrinter(indent=4, stream=file)
    pp.pprint(message)


def draw(X, Y):
    plt.plot(X, Y, 'ro')
    # Reverse Y-Axis
    plt.gca().invert_yaxis()
    plt.show()

def main(argv):
    opts, args = getopt.getopt(argv,'')
    if args[0] == '1':
        part1()
    if args[0] == '2':
        part2()


# SOLUTION GOES HERE

def part1():
    global input_data, result
    slope = (1, 3)
    height = len(input_data)
    print(height, len(input_data[0]))
    current_height = 0
    pos = (0, 0)
    while pos[0] < height - 1:
        pos = pos + slope
        pos = tuple(map(operator.add, pos, slope))
        real_pos = (pos[0], pos[1] % (len(input_data[0])))
        # print(input_data[real_pos[0]][real_pos[1]])
        if (input_data[real_pos[0]][real_pos[1]] == '#'):
            result += 1


def part2():
    global input_data, result
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    height = len(input_data)
    print(height, len(input_data[0]))
    current_height = 0
    total = 1
    res = 0
    for slope in slopes:
        pos = (0, 0)
        while pos[0] < height - 1:
            pos = pos + slope
            pos = tuple(map(operator.add, pos, slope))
            real_pos = (pos[0], pos[1] % (len(input_data[0])))
            # print(input_data[real_pos[0]][real_pos[1]])
            if (input_data[real_pos[0]][real_pos[1]] == '#'):
                res += 1
        print(res)
        total *= res
        res = 0
    result = total


if __name__ == "__main__":
    main(sys.argv[1:])


# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
