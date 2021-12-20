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

# with open(input_file) as f:
#     input_data = f.read()
with open(input_file) as f:
    input_data = f.read().split()
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

def get_distance(p1, p2):
    return (p2, abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]))

def main():
    global input_data, result
    steps1 = input_data[0].split(',')
    center = (100000, 100000)
    table = np.zeros((200001, 200001))
    table[center] = 1
    positions = []
    values = []
    c1 = 0
    pos1 = center
    for step in steps1:
        direction = step[0]
        count = int(step[1:])
        if direction == 'D':
            for x in range(count): 
                c1 += 1
                p = (pos1[0]+x,pos1[1])
                table[p] = 1 
            pos1 = (pos1[0]+count, pos1[1])
        elif direction == 'U':
            for x in range(count): 
                c1 += 1
                p = (pos1[0]-x,pos1[1])
                table[p] = 1 
            pos1 = (pos1[0]-count, pos1[1])
        elif direction == 'R':
            for x in range(count): 
                c1 += 1
                p = (pos1[0],pos1[1]+x)
                table[p] = 1
            pos1 = (pos1[0], pos1[1]+count)
        elif direction == 'L':
            for x in range(count): 
                c1 += 1
                p = (pos1[0],pos1[1]-x)
                table[p] = 1 
            pos1 = (pos1[0], pos1[1]-count)

    steps2 = input_data[1].split(',')

    # cable 2
    pos2 = center
    for step in steps2:
        direction = step[0]
        count = int(step[1:])
        if direction == 'D':
            for x in range(count): 
                p = (pos2[0]+x,pos2[1])
                if table[p] == 1:
                    table[p] = 3
                    positions.append(p)
                elif table[p] == 3:
                    table[p] = 3
                else:
                    table[p] = 2 
            pos2 = (pos2[0]+count, pos2[1])
        elif direction == 'U':
            for x in range(count): 
                p = (pos2[0]-x,pos2[1])
                if table[p] == 1:
                    table[p] = 3
                    positions.append(p)
                elif table[p] == 3:
                    table[p] = 3
                else:
                    table[p] = 2 
            pos2 = (pos2[0]-count, pos2[1])
        elif direction == 'R':
            for x in range(count): 
                p = (pos2[0],pos2[1]+x)
                if table[p] == 1:
                    table[p] = 3
                    positions.append(p)
                elif table[p] == 3:
                    table[p] = 3
                else:
                    table[p] = 2
            pos2 = (pos2[0], pos2[1]+count)
        elif direction == 'L':
            for x in range(count): 
                p = (pos2[0],pos2[1]-x)
                if table[p] == 1:
                    table[p] = 3
                    positions.append(p)
                elif table[p] == 3:
                    table[p] = 3
                else:
                    table[p] = 2
            pos2 = (pos2[0], pos2[1]-count)

    distances = [get_distance(center, p) for p in positions]
    distances.sort(key = lambda x: x[1])
    ppprint(positions)

def main2():
    global input_data, result, real_input_data
    positions = [
        (100000, 100000),
        (100000, 99096),
        (100000, 99070),
        (99875, 98778),
        (99787, 98768),
        (99764, 98768),
        (99751, 98768),
        (99573, 98768),
        (99454, 99143),
        (99454, 99319),
        (99721, 99631),
        (100006, 99631),
        (100006, 99392),
        (99721, 99392),
        (99514, 99728),
        (99095, 100723),
        (98910, 100723),
        (98622, 100723),
        (98260, 100323),
        (98161, 99938)
    ]
    steps1 = input_data[0].split(',')
    center = (100000, 100000)
    table = np.zeros((200001, 200001))
    table[center] = 1
    positions1 = positions[:]
    positions2 = positions[:]
    values = []
    c1 = 0
    pos1 = center
    for step in steps1:
        direction = step[0]
        count = int(step[1:])
        if direction == 'D':
            for x in range(count): 
                c1 += 1
                p = (pos1[0]+x,pos1[1])
                if p in positions:
                    positions1[positions.index(p)] = c1
                table[p] = 1 
            pos1 = (pos1[0]+count, pos1[1])
        elif direction == 'U':
            for x in range(count): 
                c1 += 1
                p = (pos1[0]-x,pos1[1])
                if p in positions:
                    positions1[positions.index(p)] = c1
                table[p] = 1 
            pos1 = (pos1[0]-count, pos1[1])
        elif direction == 'R':
            for x in range(count): 
                c1 += 1
                p = (pos1[0],pos1[1]+x)
                if p in positions:
                    positions1[positions.index(p)] = c1
                table[p] = 1
            pos1 = (pos1[0], pos1[1]+count)
        elif direction == 'L':
            for x in range(count): 
                c1 += 1
                p = (pos1[0],pos1[1]-x)
                if p in positions:
                    positions1[positions.index(p)] = c1
                table[p] = 1 
            pos1 = (pos1[0], pos1[1]-count)

    steps2 = input_data[1].split(',')

    # cable 2
    pos2 = center
    c2 = 0
    for step in steps2:
        direction = step[0]
        count = int(step[1:])
        if direction == 'D':
            for x in range(count): 
                c2 += 1
                p = (pos2[0]+x,pos2[1])
                if p in positions:
                    positions2[positions.index(p)] = positions1[positions.index(p)] + c2
                if table[p] == 1:
                    table[p] = 3
                elif table[p] == 3:
                    table[p] = 3
                else:
                    table[p] = 2 
            pos2 = (pos2[0]+count, pos2[1])
        elif direction == 'U':
            for x in range(count): 
                c2 += 1
                p = (pos2[0]-x,pos2[1])
                if p in positions:
                    positions2[positions.index(p)] = positions1[positions.index(p)] + c2
                if table[p] == 1:
                    table[p] = 3
                elif table[p] == 3:
                    table[p] = 3
                else:
                    table[p] = 2 
            pos2 = (pos2[0]-count, pos2[1])
        elif direction == 'R':
            for x in range(count): 
                c2 += 1
                p = (pos2[0],pos2[1]+x)
                if p in positions:
                    positions2[positions.index(p)] = positions1[positions.index(p)] + c2
                if table[p] == 1:
                    table[p] = 3
                elif table[p] == 3:
                    table[p] = 3
                else:
                    table[p] = 2
            pos2 = (pos2[0], pos2[1]+count)
        elif direction == 'L':
            for x in range(count): 
                c2 += 1
                p = (pos2[0],pos2[1]-x)
                if p in positions:
                    positions2[positions.index(p)] = positions1[positions.index(p)] + c2
                if table[p] == 1:
                    table[p] = 3
                elif table[p] == 3:
                    table[p] = 3
                else:
                    table[p] = 2
            pos2 = (pos2[0], pos2[1]-count)

    positions2.sort()
    ppprint(positions1)
    ppprint(positions2)
    ppprint(positions2[1])



if __name__ == "__main__":
    # main()
    main2()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
