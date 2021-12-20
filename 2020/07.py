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
list_of_bags = {}

def part1():
    global input_data, result
    bags = {}
    colors = []
    bag = {}
    for i in input_data:
        e = i.split(' contain')
        b = e[0].strip()
        b = re.sub('[\d] ', '', b)
        b = re.sub('bags', '', b)
        b = re.sub('bag', '', b)
        b = re.sub('\.', '', b).strip()
        c = e[1].split(', ')
        bags[b] = c
    # ppprint(bags)

    bags_added = 0
    while bags_added > 0 or len(colors) == 0:
        print(len(colors))
        bags_added = 0
        for b in bags:
            c_in_colors = 0
            for c in bags[b]:
                c_trimmed = re.sub('[\d] ', '', c)
                c_trimmed = re.sub('bags', '', c_trimmed)
                c_trimmed = re.sub('bag', '', c_trimmed)
                c_trimmed = re.sub('\.', '', c_trimmed).strip()

                if c_trimmed in colors:
                    c_in_colors += 1

                if "shiny gold" in c and b not in colors:
                    print(b, bags[b])
                    colors.append(b)
                    bags_added += 1

                if (any(ba in c for ba in colors)) and b not in colors:
                    print(b, bags[b])
                    colors.append(b)
                    bags_added += 1

                # elif any(ba in c for ba in colors) and b not in colors:
            if c_in_colors == len(bags[b]) and b not in colors:
                print(b, bags[b])
                colors.append(b)
                bags_added += 1
            # print(colors)
 
    result = len(colors)

def part2():
    global input_data, result
    get_values('shiny gold')
    # print(len(list_of_bags))
    # ppprint(list_of_bags)
    # result = get_amount('wavy lime')
    result = sum([get_amount('shiny gold')])
    # result = sum([list_of_bags['shiny gold'][key] * get_amount(key) for key in list_of_bags['shiny gold']])


def get_values(color: str):
    global list_of_bags

    L = None

    for line in input_data:
        if re.match(color + " bags contain", line):
            L = line

    e = L.split(' contain')
    b = e[0].strip()
    b = re.sub('[\d] ', '', b)
    b = re.sub('bags', '', b)
    b = re.sub('bag', '', b)
    b = re.sub('\.', '', b).strip()
    color = b

    col = e[1].split(', ')
    for c in col:
        c_trimmed = re.sub('[\d] ', '', c)
        c_trimmed = re.sub('bags', '', c_trimmed)
        c_trimmed = re.sub('bag', '', c_trimmed)
        c_trimmed = re.sub('\.', '', c_trimmed).strip()

        c_count = c.split()[0]

        if c_trimmed != 'no other':
            if b not in list_of_bags:
                list_of_bags[b] = {}
            list_of_bags[b][c_trimmed] = int(c_count)
            get_values(c_trimmed)
        else:
            list_of_bags[b] = {}

    
def get_amount(color: str):
    global list_of_bags
    if list_of_bags[color] == {}:
        return 1
    else:
        print(color, [(key, list_of_bags[color][key]) for key in list_of_bags[color]])
        return 1 + sum([list_of_bags[color][key] * get_amount(key) for key in list_of_bags[color]])


if __name__ == "__main__":
    main(sys.argv[1:])


# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)


# between 43316 and 50000