# IMPORTS
from os import path
from scipy import stats
import math
import numpy as np
import pprint
import sys
import re
# import matplotlib.pyplot as plt
from numpy import unravel_index
# np.set_printoptions(threshold=np.nan)
np.set_printoptions(threshold=sys.maxsize)

# SETUP
input_file = path.splitext(path.basename(__file__))[0].split('.')[0] + '.txt'
# input_file = path.splitext(path.basename(__file__))[0] + '.test.txt'

# with open(input_file) as f:
#     input_data = f.read()
with open(input_file) as f:
    input_data = f.read().split()
# input_data = np.loadtxt(input_file, dtype=np.object)

if not input_data:
    raise Exception('No content !')

# GLOBAL VARIABLES
result = None

# FUNCTIONS
def ppprint(message, file=None):
    # np.set_printoptions(threshold=np.nan)
    pp = pprint.PrettyPrinter(indent=4, stream=file, width=250)
    pp.pprint(message)


def draw(X, Y):
    plt.plot(X, Y, 'ro')
    # Reverse Y-Axis
    plt.gca().invert_yaxis()
    plt.show()

# SOLUTION GOES HERE
def get_slope(a, b):
    if b[0] == a[0]:
        return (math.inf, b[1] > a[1])

    slope = (b[1] - a[1]) / (b[0] - a[0])
    return (slope, b[0] > a[0])

def get_slopes_for_position(p):
    global input_data

    (x, y) = p
    slopes = []


    for i in range(len(input_data)):
        # j for horizontal
        for j in range(len(input_data[i])):
            if x == i and y == j:
                continue
            if input_data[i][j] != '#':
                continue
            slope = get_slope((i, j), p)
            if slope not in slopes:
                # print(slope)
                slopes.append(slope)
    return len(slopes)


def main():
    global input_data, result
    input_data = [list(s) for s in input_data]

    result = [[0]*len(input_data[0]) for _ in range(len(input_data))] 

    # i for vertical
    for i in range(len(input_data)):
        # j for horizontal
        for j in range(len(input_data[i])):
            if input_data[i][j] == '#':
                result[i][j] = get_slopes_for_position((i,j))
            else:
                result[i][j] = 0

    max_value = get_max_value_in_2d_list(result)
    result = np.array(result)
    position =  np.where(result == max_value)
    print(position, max_value)



def get_max_value_in_2d_list(my_list):
    flattened_list = [y for x in my_list for y in x]
    return max(flattened_list)

def format_result():
    global result
    result = [''.join(result[x]) for x in range(len(result))]



if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)


# not 49
# 377 too high
# not 151
# not 156
# not 170
# not 368
# not 342
# not 358
# not 359
# not 357
# not 360