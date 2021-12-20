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
    if b[1] == a[1]:
        slope = -math.pi/2 if b[0] > a[0] else math.pi/2
    else:
        slope = (a[0] - b[0]) / (a[1] - b[1])
        slope = np.arctan(slope) + math.pi if a[1] < b[1] else np.arctan(slope)


    a = np.asarray(a)
    b = np.asarray(b)
    dist = np.linalg.norm(b-a)
    return {
        "position": a,
        "slope": (slope + math.pi/2) % (2*math.pi),
        "distance": dist
    }

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
            slopes.append(slope)

    return slopes

def get_unique_slopes(points):
    res = []
    for p in points:
        if p['slope'] not in res:
            res.append(p['slope'])

    return sorted(res)


def get_points_where_slope_is(slope, points):
    res = []
    for p in points:
        if p['slope'] == slope:
            res.append(p)

    return sorted(res, key = lambda i: i['distance']) 


def main():
    global input_data, result
    input_data = [list(s) for s in input_data]

    position = (36, 26)

    points = get_slopes_for_position(position)
    unique_slopes = get_unique_slopes(points)

    for s in unique_slopes:
        ps = get_points_where_slope_is(s, points)
        for i, p in enumerate(ps):
            p['slope'] += (2*math.pi)*i

    result = sorted(points, key = lambda i: i['slope']) 


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

