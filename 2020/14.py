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
    if args[0] == '21':
        return part21()


# SOLUTION GOES HERE

def part1():
    global input_data
    mask = None
    addresses = {}
    for line in input_data:
        if re.match('^mask', line):
            match = re.search('mask = (.*)', line)
            mask = match.group(1)
        else:
            match = re.search('mem\[(\d+)\] = (.*)', line)
            ad = int(match.group(1))
            v = int_to_bin(int(match.group(2)))
            addresses[ad] = change_ad(v, mask)

    l = [bin_to_int(v) for v in list(addresses.values())]

    return sum(l)


def part2():
    global input_data
    mask = None
    addresses = {}
    for line in input_data:
        if re.match('^mask', line):
            match = re.search('mask = (.*)', line)
            mask = match.group(1)
        else:
            match = re.search('mem\[(\d+)\] = (.*)', line)
            int_address = int(match.group(1))
            addresses_to_rewrite = get_addresses(int_address, mask)
            v = int_to_bin(int(match.group(2)))
            if addresses_to_rewrite:
                for adr in addresses_to_rewrite:
                    int_adr = bin_to_int(adr)
                    addresses[int_adr] = int(match.group(2))

    return sum(addresses.values())


def change_ad(bin_value, mask):
    for i, c in enumerate(bin_value):
        if mask[i] != 'X':
            bin_value_list = list(bin_value)
            bin_value_list[i] = mask[i]
            bin_value = ''.join(bin_value_list)
    return bin_value

def int_to_bin(v):
    return "{0:b}".format(v).zfill(36)


def bin_to_int(v):
    return int('{}'.format(v), 2)

def get_addresses(int_address, mask):
    bin_address = int_to_bin(int_address)
    bin_address_list = list(bin_address)
    poss = []
    X_indices = []
    for i, c in enumerate(mask):
        if c == '1':
            bin_address_list[i] = '1'
        elif c == 'X':
            X_indices.append(i)

    bin_address = ''.join(bin_address_list)

    poss = get_declinations(bin_address, X_indices)
    return poss


def get_declinations(bin_adr, x_ind):
    poss = []
    for l in ['0', '1']:
        bin_adr_list = list(bin_adr)
        bin_adr_list[x_ind[0]] = l
        if len(x_ind) > 1:
            poss = poss + get_declinations(''.join(bin_adr_list), x_ind[1:])
        else:
            poss.append(''.join(bin_adr_list))
    return list(set(poss))

if __name__ == "__main__":
    result = main(sys.argv[1:])


# OUTPUT RESULT
try:
    print(result)
except NameError:
    print("Result is not defined")
