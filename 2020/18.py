# IMPORTS
from os import path
from scipy import stats
from functools import reduce
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
# input_file = path.splitext(path.basename(__file__))[0] + '.test.txt'
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
    total = 0
    for line in input_data:
        r = compute_operation(line)
        total += r
        print('>', total, r)
    print('--------')
    return total


def compute_operation(line: str):
    result = 0
    regex = '\(([^()]+)\)'
    match = re.search(regex, line)
    if match:
        print(match.groups())
        parenthesis = match.group(0)[1:-1]
        print(parenthesis)
        line = line.replace(match.group(0), '{}'.format(compute_operation(parenthesis)), 1)
        print(line)
        result = compute_operation(line)
        # print(match.group(0))
    else:
        result = my_eval(line)
        print(result)
    # total = 0
    # operation


    return result


def my_eval(line: str):
    line = line.replace(' ', '')
    reg = '(\d+[+*]\d+)'
    match = re.search(reg, line)
    if not match:
        print(line)
        return int(line)
    else:
        ope = match.group(0)
        print(ope)
        return my_eval('{}{}'.format(eval(ope), line.replace(ope, '', 1)))


def part2():
    global input_data
    total = 0
    for line in input_data:
        r = compute_operation2(line)
        total += r
        print('>', total, r)
        # exit()
    print('--------')
    return total



def compute_operation2(line: str):
    result = 0
    regex = '\(([^()]+)\)'
    match = re.search(regex, line)
    if match:
        print(match.groups())
        parenthesis = match.group(0)[1:-1]
        print(parenthesis)
        line = line.replace(match.group(0), '{}'.format(compute_operation2(parenthesis)), 1)
        print(line)
        result = compute_operation2(line)
        # print(match.group(0))
    else:
        result = my_eval2(line)
        print(result)
    # total = 0
    # operation


    return result    


def my_eval2(line: str):
    line = line.replace(' ', '')
    reg = '(\d+[+]\d+)'
    match = re.search(reg, line)
    if not match:
        print(line)
        return eval(line)
    else:
        ope = match.group(0)
        print(ope, line.replace(ope, '{}'.format(eval(ope)), 1))
        # return my_eval2('{}{}'.format(eval(ope), line.replace(ope, '', 1)))
        return compute_operation2('{}'.format(line.replace(ope, '{}'.format(eval(ope)), 1)))
        # return my_eval2('{}'.format(line.replace(ope, '{}'.format(eval(ope)), 1)))


if __name__ == "__main__":
    result = main(sys.argv[1:])


# OUTPUT RESULT
try:
    print(result)
except NameError:
    print("Result is not defined")
