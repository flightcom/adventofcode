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
    turn = 0
    spoken = []
    initials = input_data[0].split(',')
    initials.reverse()

    while turn < 2020:
        if len(initials):
            val = initials.pop()
            spoken.append(val)
        else:
            last = spoken[-1]
            spo = np.array(spoken)
            indexes = np.where(spo == last)[0]
            if len(indexes) <= 1:
                spoken.append('0')
            else:
                # print(indexes, indexes[-1] - indexes[-2])
                spoken.append('{}'.format(indexes[-1] - indexes[-2]))
                
        turn += 1

    return spoken[-1]




def part2():
    global input_data
    turn = 0
    spoken = {}
    initials = input_data[0].split(',')
    initials.reverse()

    while turn < 30000000:
    # while turn < 2020:
        last = None
        if 'last' in spoken:
            last = spoken['last']

        if len(initials):
            val = initials.pop()
        else:
            if last and last in spoken:
                # print(last, turn, int(spoken[last]), turn - int(spoken[last]))
                val = turn - int(spoken[last])
            else:
                # print('{} not in spoken'.format(last))
                val = '0'
                
        if last:
            spoken[last] = '{}'.format(turn)
        spoken['last'] = '{}'.format(val)
        # print(val, spoken)
        turn += 1

        if turn % 1000000 == 0:
            print(turn)

    return spoken['last']


if __name__ == "__main__":
    result = main(sys.argv[1:])


# OUTPUT RESULT
try:
    print(result)
except NameError:
    print("Result is not defined")

