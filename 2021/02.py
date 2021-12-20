# IMPORTS
from os import path
# from scipy import stats
import math
# import numpy as np
import pprint
import re
# import matplotlib.pyplot as plt
# from numpy import unravel_index
import sys, getopt

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
    # (x, y) => x = horizontal position, y = vertical position
    pos = (0, 0)
    
    for entry in input_data:
        (cmd, val) = entry.split()
        val = int(val)
        if cmd == 'forward':
            pos = (pos[0] + val, pos[1])
        elif cmd == 'down':
            pos = (pos[0], pos[1] + val)
        else:
            pos = (pos[0], pos[1] - val)

    result = pos[0] * pos[1]

def part2():
    global input_data, result
    pos = (0, 0)
    aim = 0
    
    for entry in input_data:
        (cmd, val) = entry.split()
        val = int(val)
        if cmd == 'forward':
            pos = (pos[0] + val, pos[1] + val * aim)
        elif cmd == 'down':
            aim += val
        else:
            aim -= val
    result = pos[0] * pos[1]


if __name__ == "__main__":
    main(sys.argv[1:])


# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
