# IMPORTS
from os import path
from scipy import stats
import math
import numpy as np
import pprint
import re
import copy
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
        return part1()
    if args[0] == '2':
        return part2()


# SOLUTION GOES HERE

def part1():
    global input_data, result
    preamble_length = 25
    preamble = input_data[:preamble_length]

    i = 0

    for index in range(preamble_length, len(input_data) - 1):
        start = preamble_length - preamble_length + i
        end = preamble_length + i
        is_ok = check_preamble(int(input_data[index]), input_data[start:end])
        if not is_ok:
            return int(input_data[index])
            break
        i += 1
    
    return


def part2():
    global input_data, result
    num = part1()
    for i in range(len(input_data)):
        summ = 0
        for j in range(len(input_data) - i):
            summ += int(input_data[i+j])
            if summ == num:
                return sum([int(x) for x in [min(input_data[i:i+j]), max(input_data[i:i+j])]])
            


def check_preamble(value, preamble):
    for i in preamble:
        for j in preamble:
            if i != j and int(i) + int(j) == value:
                return True

    return False




if __name__ == "__main__":
    result = main(sys.argv[1:])


# OUTPUT RESULT
try:
    print(result)
except NameError:
    print("Result is not defined")
