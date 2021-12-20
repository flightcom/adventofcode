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
    global input_data
    jolt = 0
    jolt_diffs = []

    c = len(input_data)

    while len(jolt_diffs) < c:
        diffs = [int(x) - jolt for x in input_data]
        index_min = np.argmin(diffs)
        jolt_diffs.append(int(input_data[index_min]) - jolt)
        jolt = int(input_data[index_min])
        input_data.pop(index_min)

    return jolt_diffs.count(1) * (jolt_diffs.count(3) + 1)


poss = []

def part2():
    global input_data, poss

    jolt = 0
    jolt_diffs = []

    m = max([int(x) for x in input_data]) + 3
    print(m)
    # input_data = ['0'] + input_data + ['{}'.format(m)]
    # input_data = input_data + ['{}'.format(m)]
 
    c = len(input_data)

    while len(jolt_diffs) < c:
        diffs = [int(x) - jolt for x in input_data]
        index_min = np.argmin(diffs)
        jolt_diffs.append(int(input_data[index_min]) - jolt)
        jolt = int(input_data[index_min])
        input_data.pop(index_min)

    print(jolt_diffs)
    print('========')
    poss.append(jolt_diffs)

    compute(jolt_diffs)

    return len(poss)


def compute(l):
    global poss
    # print(resum(l))
    # print(l)

    for i in range(len(l)-1):
        if i < len(l) - 1 and l[i] + l[i+1] <= 3:

            if i == 0:
                new_l = [l[i]+l[i+1]] + l[i+2:]
            else:
                new_l = l[0:i] + [l[i]+l[i+1]] + l[i+2:]

            if new_l not in poss:
                poss.append(new_l)
                compute(new_l)

             
# def resum(l):
#     return [l[0]] + [l[i] + l[i+1] for i in range(1, len(l)-1)]

if __name__ == "__main__":
    result = main(sys.argv[1:])


# OUTPUT RESULT
try:
    print(result)
except NameError:
    print("Result is not defined")
