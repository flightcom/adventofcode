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

    orbites_you = get_orbites(orbites, 'H4S', [])
    orbites_san = get_orbites(orbites, 'NRN', [])
    # orbites_you = set(orbites_you)
    # orbites_san = set(orbites_san)
    # print(orbites_you.intersection(orbites_san))
    orbites_you.reverse()
    orbites_san.reverse()
    print(orbites_you)
    print(orbites_san)
    exit()

    common_points = ['4BZ', 'GLT', 'DWT', 'TXJ', 'WWP', 'PH9', 'FGQ', 'CZD', 'SKM', 'P6R', 'D94', 'V2B', 'J35', 'TKM', 'MGQ', '4CM', 'JYF', 'HN2', 'H51', 'K52', '5PT', 'TZV', 'R8P', 'YWT', 'G7Y', '3C4', 'RYC', '31Y', 'XMN', 'ZP3', 'T37', 'BN7', 'Y14', 'SCL', 'VNQ', '7FG', '9JN', 'JDQ', 'CKD', 'WJB', 'WD7', 'GTK', 'T9V', 'V85', 'HPF', 'WY1', '8N1', 'DP9', 'JZH', 'LLH', 'BHD', 'LML', 'SJ4', 'H6N', '8TK', 'DGY', 'HW6', 'QNG', '743', 'D1G', '7CD', 'H3J', 'J74', '4SV', '6YM', '21D']
    # print(common_points)

    counts = [(obj, get_count(orbites, obj, 0)) for obj in common_points]
    counts = sorted(counts, key=lambda tup: tup[1])
    # ppprint(counts)
    # exit()

    common_point = 'WWP'
    count_you = get_count_from(common_point, orbites, 'H4S', 0)
    count_san = get_count_from(common_point, orbites, 'NRN', 0)
    print(count_you, count_san)
    # ppprint(orbites_san)
    result = count_you + count_san

def get_orbites(orbites, obj, obj_orbites):
    if obj != 'COM':
        obj_orbites.append(obj)
        return get_orbites(orbites, orbites[obj], obj_orbites)
    else:
        return obj_orbites

def get_count(orbites, obj, count):
    if obj != 'COM':
        return get_count(orbites, orbites[obj], count+1)
    else:
        return count

def get_count_from(fro, orbites, obj, count):
    if obj != fro:
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


# 558 too high
# 556 too high
# 554 too high

