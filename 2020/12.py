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
    position = [0, 0]
    direction = 'E'

    # for line in input_data:
    #     match = re.search('(\w)([\d]{2})', line)

        # ins = match.group(1)
        # val = match.group(2)
        # print(ins, val)
    tuples = [(m.group(1), int(m.group(2))) for l in input_data for m in [re.search('(\w)([\d]+)', l)] if m]
    
    for t in tuples:
        if t[0] == 'E':
            position[1] += t[1]
        elif t[0] == 'N':
            position[0] -= t[1]
        elif t[0] == 'W':
            position[1] -= t[1]
        elif t[0] == 'S':
            position[1] += t[1]
        elif t[0] == 'S':
            position[1] += t[1]

        elif t[0] == 'R':
            if t[1] == 90:
                if direction == 'E':
                    direction = 'S'
                elif direction == 'N':
                    direction = 'E'
                elif direction == 'W':
                    direction = 'N'
                elif direction == 'S':
                    direction = 'W'
            elif t[1] == 180:
                if direction == 'E':
                    direction = 'W'
                elif direction == 'N':
                    direction = 'S'
                elif direction == 'W':
                    direction = 'E'
                elif direction == 'S':
                    direction = 'N'
            elif t[1] == 270:
                if direction == 'E':
                    direction = 'N'
                elif direction == 'N':
                    direction = 'W'
                elif direction == 'W':
                    direction = 'S'
                elif direction == 'S':
                    direction = 'E'
        elif t[0] == 'L':
            if t[1] == 90:
                if direction == 'E':
                    direction = 'N'
                elif direction == 'N':
                    direction = 'W'
                elif direction == 'W':
                    direction = 'S'
                elif direction == 'S':
                    direction = 'E'
            elif t[1] == 180:
                if direction == 'E':
                    direction = 'W'
                elif direction == 'N':
                    direction = 'S'
                elif direction == 'W':
                    direction = 'E'
                elif direction == 'S':
                    direction = 'N'
            elif t[1] == 270:
                if direction == 'E':
                    direction = 'S'
                elif direction == 'N':
                    direction = 'E'
                elif direction == 'W':
                    direction = 'N'
                elif direction == 'S':
                    direction = 'W'

        elif t[0] == 'F':
            if direction == 'E':
                position[1] += t[1]
            elif direction == 'N':
                position[0] -= t[1]
            elif direction == 'W':
                position[1] -= t[1]
            elif direction == 'S':
                position[0] += t[1]

    print(n)
    return sum([abs(x) for x in position])



def part2():
    global input_data
    position = [0, 0]
    waypoint = [1, 10, 0, 0]

    tuples = [(m.group(1), int(m.group(2))) for l in input_data for m in [re.search('(\w)([\d]+)', l)] if m]

    for t in tuples:
        wp = []
        if t[0] == 'E':
            index_to_reduce = 3
            index_to_increase = 1
        elif t[0] == 'N':
            index_to_reduce = 2
            index_to_increase = 0
        elif t[0] == 'W':
            index_to_reduce = 1
            index_to_increase = 3
        elif t[0] == 'S':
            index_to_reduce = 0
            index_to_increase = 2

        if t[0] in ['E','N','W','S']:
            if waypoint[index_to_reduce] > 0:
                if waypoint[index_to_reduce] > t[1]:
                    waypoint[index_to_reduce] -= t[1]
                else:
                    waypoint[index_to_increase] += t[1] - waypoint[index_to_reduce]
                    waypoint[index_to_reduce] = 0
            else:
                waypoint[index_to_increase] += t[1]

        elif t[0] == 'R':
            if t[1] >= 90:
                waypoint = waypoint[-1:] + waypoint[:-1]
            if t[1] >= 180:
                waypoint = waypoint[-1:] + waypoint[:-1]
            if t[1] >= 270:
                waypoint = waypoint[-1:] + waypoint[:-1]
        elif t[0] == 'L':
            if t[1] >= 90:
                waypoint = waypoint[1:] + waypoint[:1]
            if t[1] >= 180:
                waypoint = waypoint[1:] + waypoint[:1]
            if t[1] >= 270:
                waypoint = waypoint[1:] + waypoint[:1]

        elif t[0] == 'F':
            position[0] += t[1] * waypoint[2]
            position[0] -= t[1] * waypoint[0]
            position[1] += t[1] * waypoint[1]
            position[1] -= t[1] * waypoint[3]
    
        print(position, waypoint)

    return sum([abs(x) for x in position])


if __name__ == "__main__":
    result = main(sys.argv[1:])


# OUTPUT RESULT
try:
    print(result)
except NameError:
    print("Result is not defined")


# 79717 too high