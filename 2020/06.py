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
    groups = []
    group = []
    for line in input_data:
        if line == '':
            group = list(set(group))
            groups.append(group)
            group = []
            continue
        else:
            for c in line:
                group.append(c)
    group = list(set(group))
    groups.append(group)
    result = sum([len(g) for g in groups])

def part2():
    global input_data, result
    alphabet = set(['a','b','c','d','e','f','g','h','k','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    groups = []
    group = []
    for line in input_data:
        if line == '':
            groups.append(alphabet.intersection(*group))
            group = []
            continue
        else:
            ind = []
            for c in line:
                ind.append(c)
            group.append(ind)

    groups.append(alphabet.intersection(*group))
    result = sum([len(g) for g in groups])


if __name__ == "__main__":
    main(sys.argv[1:])


# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
