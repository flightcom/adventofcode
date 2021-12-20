# IMPORTS
from os import path
from scipy import stats
import math
import numpy as np
import pprint
import re
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
        part1()
    if args[0] == '2':
        part2()


# SOLUTION GOES HERE

def part1():
    global input_data, result
    passports = []
    pp = {}
    for line in input_data:
        if line == '':
            passports.append(pp)
            pp = {}
            continue
        else:
            entries = line.split()
            for entry in entries:
                t = entry.split(':')
                pp[t[0]] = t[1]

    for p in passports:
        if "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p and "hcl" in p and "ecl" in p and "pid" in p:
            result += 1
    print(len(passports))

def part2():
    global input_data, result
    passports = []
    valid_passports = []
    pp = {}
    for line in input_data:
        if line == '':
            passports.append(pp)
            pp = {}
            continue
        else:
            entries = line.split()
            for entry in entries:
                t = entry.split(':')
                pp[t[0]] = t[1]

    for p in passports:
        if "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p and "hcl" in p and "ecl" in p and "pid" in p:
            valid_passports.append(p)

    print(len(valid_passports))

    for p in valid_passports:
        if  1920 <= int(p['byr']) <= 2020 \
            and 2010 <= int(p['iyr']) <= 2020 \
            and 2020 <= int(p['eyr']) <= 2030 \
            and validateHGT(p['hgt']) \
            and validateHCL(p['hcl']) \
            and validateECL(p['ecl']) \
            and validatePID(p['pid']) \
            :
            result += 1


def validateHGT(hgt):
    if hgt.endswith('in'): 
        return 59 <= int(hgt.replace('in', '')) <= 76
    elif hgt.endswith('cm'):
        return 150 <= int(hgt.replace('cm', '')) <= 193


def validateHCL(hcl):
    return hcl[0] == '#' and re.match(r'[0-9a-f]{6}', hcl[1:])

def validateECL(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validatePID(pid):
    return re.match(r'[0-9]{9}', pid)


if __name__ == "__main__":
    main(sys.argv[1:])


# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
