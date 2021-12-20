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
from math import gcd

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
def ppcm(m,n):
   return m*n//pgcd(m,n) 

def pgcd(m,n): 
    while m%n: 
        r=m%n 
        m=n 
        n=r 
    return n 

def part1():
    global input_data
    timestamp = int(input_data[0])
    ids = [int(x) for x in input_data[1].split(',') if x != 'x']
    num = {}
    for id in ids:
        i = 0
        while i * id < timestamp:
            i+= 1
        num[id] = i * id
    return num


def part2():
    global input_data
    ids = [(int(x), i) if x != 'x' else x for i, x in enumerate(input_data[1].split(','))]
    ids_cured = [x for x in ids if x[0] != 'x']
    # gid = max([x[0] for x in ids_cured])
    t_gid = [x for x in ids_cured if x[0] == max([y[0] for y in ids_cured])][0]
    gid = t_gid[0]
    ids_retimed = [(x[0], x[1] - t_gid[1]) for x in ids_cured]
    ids_filtered = [x for x in ids_retimed if x[1] != 0]

    # print(ids_filtered)

    for i in ids_filtered:
        if isPrime(i[0]):
            print('{} is prime'.format(i))
        else:
            print('{} is not prime'.format(i))

    exit()

    print(ids_filtered)
    found = False
    ts = None
    i = 100000000000
    while not found:
        found = True
        for t_id in ids_filtered:
            (id, d) = t_id
            if (gid * i + d) % id != 0:
                found = False
                break
        i += 1
        if i % 100000000 == 0:
            print(gid * i, t_id)

    return i * gid - ids_filtered[0][1]


def isPrime(n) : 
 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True
 

if __name__ == "__main__":
    result = main(sys.argv[1:])


# OUTPUT RESULT
try:
    print(result)
except NameError:
    print("Result is not defined")


# 100000000000000
# 2622062845747423 too high
# 154238990926319 too low
# 103089800000000
# 112262200000000
# 1247479301
