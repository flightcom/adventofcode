# IMPORTS
from os import path
from scipy import stats
import math
import numpy as np
import pprint
import re
# import matplotlib.pyplot as plt
from numpy import unravel_index

# SETUP
input_file = path.splitext(path.basename(__file__))[0] + '.txt'
# input_file = 'test.txt'
if not path.isfile(input_file):
    input_file = '1.txt'

with open(input_file) as f:
    input_data = f.read()
# with open(input_file) as f:
#     input_data = f.read().split()
# with open(input_file) as f:
#     input_data = f.read().splitlines()


if not input_data:
    raise Exception('No content !')

result = 0
split_data = None
real_input_data = None
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

# SOLUTION GOES HERE

def pre():
    global input_data
    # replace position 1 with the value 12 and replace position 2 with the value 2
    input_data[1] = 12
    input_data[2] = 2

def pre2(v1, v2):
    global input_data
    input_data[1] = v1
    input_data[2] = v2

def split():
    global input_data, split_data
    split_data = []
    n = 0
    while n < len(input_data):
        if input_data[n] != 99:
            l = 4
        else:
            l = 1
        split_data.append(input_data[n:n+l])
        n += l

def process():
    global input_data, split_data, result
    for n in range(len(split_data)):
        # ppprint(n)
        # ppprint(split_data[n])
        opcode = split_data[n][0]
        if opcode != 99:
            val1 = input_data[split_data[n][1]]
            val2 = input_data[split_data[n][2]]
            input_data[split_data[n][3]] = val1 + val2 if opcode == 1 else val1 * val2
        else:
            break
    result = input_data[0]


def main():
    global input_data, result
    input_data = input_data.split(',')
    input_data = [int(x) for x in input_data]
    pre()
    split()
    process()
    # print(input_data)

def main2():
    global input_data, result, real_input_data
    input_data = input_data.split(',')
    input_data = [int(x) for x in input_data]
    real_input_data = input_data[:]
    inp1 = 0
    inp2 = 0
    for i in range(99):
        for j in range(99):
            run(i, j)
            if result == 19690720:
                ppprint('STOP')
                ppprint(100 * i + j)


def run(v1, v2):
    global input_data, real_input_data
    # ppprint(real_input_data)
    input_data = real_input_data[:]
    pre2(v1, v2)
    split()
    process()

if __name__ == "__main__":
    main2()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
