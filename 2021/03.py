# IMPORTS
from os import path
# from scipy import stats
import math
# import numpy as np
import pprint
import re
# import matplotlib.pyplot as plt
# from numpy import unravel_index
import sys, getopt

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
    bytes = []
    for n in range(len(input_data[0])):    
        b = [int(x[n]) for x in input_data]
        count_ones = b.count(1)
        count_zeros = b.count(0) 
        if count_ones > count_zeros:
            bytes.append(1)
        else:
            bytes.append(0)
            
    bytes = ''.join(str(e) for e in bytes)
    opposite = ''.join(['1' if i == '0' else '0' for i in bytes])
    
    gamma = int(bytes, 2)
    epsilon = int(opposite, 2)
    result = gamma * epsilon

def part2():
    global input_data, result
    # Oxygen (most)
    numlist = input_data
    print(numlist)

    for n in range(len(input_data[0])):    
        b = [int(x[n]) for x in numlist]
        count_ones = b.count(1)
        count_zeros = b.count(0)
        max_digit = '1' if max(count_ones, count_zeros) == count_ones else '0'
        if len(numlist) == 1:
            break
        numlist = [num for num in numlist if num[n] == max_digit]
        print(numlist)
    oxygen = numlist[0]
    oxygen_dec = int(numlist[0], 2)

    print('-----------')

    # CO2 (less)
    numlist = input_data

    for n in range(len(input_data[0])):    
        b = [int(x[n]) for x in numlist]
        count_ones = b.count(1)
        count_zeros = b.count(0)
        max_digit = '0' if min(count_ones, count_zeros) == count_zeros else '1'
        if len(numlist) == 1:
            break
        numlist = [num for num in numlist if num[n] == max_digit]
        print(len(numlist))
    co2 = numlist[0]
    co2_dec = int(numlist[0], 2)

    print(oxygen, oxygen_dec)
    print(co2, co2_dec)
    result = oxygen_dec * co2_dec


if __name__ == "__main__":
    main(sys.argv[1:])


# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)


# 1079645 too low