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
changes = None

def part1():
    global input_data, changes
    input_data_copy = input_data.copy()
    charar = np.chararray((len(input_data_copy), len(input_data_copy[0])))
    for i in range(len(input_data_copy)):
        for j in range(len(input_data_copy[0])):
            charar[i][j] = input_data_copy[i][j]
    input_data = charar

    while changes != 0:
        changes = 0
        # print(input_data)
        input_data = run()
        print(changes)
    occurrences = np.count_nonzero(input_data == b'#')
    return occurrences

def run():
    global input_data, changes
    input_d = input_data.copy()
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            (a, e, o) = get_number_of_adjacent_seats2(i, j)
            # print(input_data[i, j], a, e, o)
            if input_data[i, j] == b'L' and a == e:
                input_d[i, j] = b'#'
                changes += 1
            elif input_data[i, j] == b'#' and o >= 4:
                input_d[i, j] = b'L'
                changes += 1
    return input_d

def get_number_of_adjacent_seats(r: int, c: int):
    global input_data
    min_r = max(0, r-1)
    max_r = min(len(input_data), r+2)
    min_c = max(0, c-1)
    max_c = min(len(input_data[0]), c+2)
    # print(input_data[min_r:max_r,min_c:max_c])
    count_all = 0
    count_empty = 0
    count_occupied = 0
    for ri in range(min_r, max_r):
        for ci in range(min_c, max_c):
            if not (ri == r and ci == c):
                if input_data[ri, ci] in [b'L', b'#']:
                    count_all += 1
                if input_data[ri, ci] == b'L':
                    count_empty += 1
                elif input_data[ri, ci] == b'#':
                    count_occupied += 1
    return (count_all, count_empty, count_occupied)

def part2():
    global input_data
    input_data_copy = input_data.copy()
    charar = np.chararray((len(input_data_copy), len(input_data_copy[0])))
    for i in range(len(input_data_copy)):
        for j in range(len(input_data_copy[0])):
            charar[i][j] = input_data_copy[i][j]
    input_data = charar

    changes = None

    while changes != 0:
        # print(input_data)
        input_data = run2()
        print(changes)
    occurrences = np.count_nonzero(input_data == b'#')
    return occurrences

def run2():
    global input_data, changes
    changes = 0
    input_d = input_data.copy()
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            (a, e, o) = get_number_of_adjacent_seats2(i, j)
            print(a, e, o)
            if input_data[i, j] == b'L' and a == e:
                input_d[i, j] = b'#'
                changes += 1
            elif input_data[i, j] == b'#' and o >= 5:
                input_d[i, j] = b'L'
                changes += 1
    return input_d


def get_number_of_adjacent_seats2(r: int, c: int):
    global input_data
    min_r = max(0, r-1)
    max_r = min(len(input_data), r+2)
    min_c = max(0, c-1)
    max_c = min(len(input_data[0]), c+2)
    # print(input_data[min_r:max_r,min_c:max_c])
    count_all = 0
    count_empty = 0
    count_occupied = 0
    for ri in range(min_r, max_r):
        for ci in range(min_c, max_c):
            if not (ri == r and ci == c):
                if input_data[ri, ci] in [b'L', b'#']:
                    count_all += 1
                if input_data[ri, ci] == b'L':
                    count_empty += 1
                elif input_data[ri, ci] == b'#':
                    count_occupied += 1
    return (count_all, count_empty, count_occupied)

if __name__ == "__main__":
    result = main(sys.argv[1:])


# OUTPUT RESULT
try:
    print(result)
except NameError:
    print("Result is not defined")

