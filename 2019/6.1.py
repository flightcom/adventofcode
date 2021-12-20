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
input_file = path.splitext(path.basename(__file__))[0].split('.')[0] + '.txt'
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



def main():
    global input_data, result
    # print(input_data)
    orbites = {}
    for orbite in input_data:
        # print(orbite)
        (star, obj) = orbite.split(')')
        orbites[obj] = star

    counts = [get_count(orbites, obj, 0) for obj in orbites.keys()]
    result = sum(counts)

def get_count(orbites, obj, count):
    # if obj in orbites.keys():
    if obj != 'COM':
        # print(obj, orbites[obj])
        return get_count(orbites, orbites[obj], count+1)
    else:
        return count


if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
