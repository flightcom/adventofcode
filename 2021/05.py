# IMPORTS
from os import path
# from scipy import stats
import math
import numpy as np
import pprint
import re
# import matplotlib.pyplot as plt
# from numpy import unravel_index
import sys, getopt

# SETUP
input_file = path.splitext(path.basename(__file__))[0] + '.txt'
input_file = 'test.txt'
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

def remove_vectors(vectors):
    for i, v in enumerate(vectors):
        (p1, p2) = v
        if p1[0] != p2[0] and p1[1] != p2[1]:
            vectors.pop(i)
            
    return vectors

def part1():
    global input_data, result
    vectors = []
    points = []
    for line in input_data:
        (p1, p2) = line.split(' -> ')
        p1 = [int(x) for x in p1.split(',')]
        p2 = [int(x) for x in p2.split(',')]
        points.append(p1)
        points.append(p2)
        vectors.append((p1, p2))
    vectors = remove_vectors(vectors)

    max_x = max([x[0] for x in points])
    max_y = max([x[1] for x in points])
    mx = np.zeros((max_x+1, max_y+1))

    for v in vectors:
        (p1, p2) = v
        if p1[0] == p2[0]:
            min_y = min(p1[1], p2[1])
            max_y = max(p1[1], p2[1])
            diff = max_y - min_y
            for y in range(diff+1):
                mx[p1[0],min_y+y] += 1
        elif p1[1] == p2[1]:
            min_x = min(p1[0], p2[0])
            max_x = max(p1[0], p2[0])
            diff = max_x - min_x
            for x in range(diff+1):
                mx[min_x+x, p1[1]] += 1
                
    count = (mx >= 2).sum()
    result = count  
        

def part2():
    global input_data, result
    vectors = []
    points = []
    for line in input_data:
        (p1, p2) = line.split(' -> ')
        p1 = [int(x) for x in p1.split(',')]
        p2 = [int(x) for x in p2.split(',')]
        points.append(p1)
        points.append(p2)
        vectors.append((p1, p2))
    vectors = remove_vectors(vectors)

    max_x = max([x[0] for x in points])
    max_y = max([x[1] for x in points])
    mx = np.zeros((max_x+1, max_y+1))

    for v in vectors:
        (p1, p2) = v
        min_y = min(p1[1], p2[1])
        max_y = max(p1[1], p2[1])
        min_x = min(p1[0], p2[0])
        max_x = max(p1[0], p2[0])
        diff_y = max_y - min_y
        diff_x = max_x - min_x

        if p1[0] == p2[0]:
            for y in range(diff_y+1):
                mx[p1[0],min_y+y] += 1

        elif p1[1] == p2[1]:
            for x in range(diff_x+1):
                mx[min_x+x, p1[1]] += 1

        elif max_y - min_y == max_x - min_x:
            diff = max_y - min_y
            if p2[0] > p1[0] and p2[1] > p1[1]:
                print(p1, p2, 1)
                for x in range(diff+1):
                    mx[p1[0] + x, p1[1] + x] += 1
            elif p2[0] > p1[0] and p2[1] < p1[1]:
                print(p1, p2, 2)
                for x in range(diff+1):
                    mx[p1[0] + x, p1[1] - x] += 1
            elif p2[0] < p1[0] and p2[1] > p1[1]:
                print(p1, p2, 3)
                for x in range(diff+1):
                    mx[p1[0] - x, p1[1] + x] += 1
            elif p2[0] < p1[0] and p2[1] < p1[1]:
                print(p1, p2, 4)
                for x in range(diff+1):
                    mx[p2[0] + x, p2[1] + x] += 1
                
                
    count = (mx >= 2).sum()
    result = count  


if __name__ == "__main__":
    main(sys.argv[1:])


# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)

# not 3
# 7163 too low (2)
# 7166 too low (2)
# 7167 too low (2)