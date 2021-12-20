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
    prev = int(input_data[0])
    count = 0
    for n in input_data[1:]:
        if int(n) > prev:
            print(prev, n)
            if prev != 0:
                count = count + 1
        prev = int(n)
    result = count


def part2():
    global input_data, result
    input_data = [int(i) for i in input_data]
    windows = [sum([input_data[i], input_data[i+1], input_data[i+2]]) for (i, x) in enumerate(input_data[:-2])]

    prev = windows[0]
    count = 0
    for n in windows[1:]:
        if int(n) > prev:
            if prev != 0:
                count = count + 1
        prev = int(n)
    result = count


if __name__ == "__main__":
    main(sys.argv[1:])


# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
