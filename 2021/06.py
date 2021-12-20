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
def run(fish):
    for i, x in enumerate(fish):
        if x == 0:
            fish.append(9)
            fish[i] = 6
        else:
            fish[i] -= 1
    return fish

def part1():
    global input_data, result
    fish = input_data[0].split(',')
    fish = [int(x) for x in fish]
    days = 0
    print(len(fish))
    while days < 80:
        fish2 = fish
        fish = [x-1 if x > 0 else 6 for x in fish]
        print([9 for x in fish2 if x == 0])
        # for i, x in enumerate(fish):
        #     if x == 0:
        #         fish.append(9)
        #         fish[i] = 6
        #     else:
        #         fish[i] -= 1
        days += 1        
    print(len(fish))

def part2():
    global input_data, result
    fish = input_data[0].split(',')
    # fish = [int(x) for x in fish]
    # days = 0
    # print(len(fish))
    # while days < 256:
    #     fish = run(fish)
    #     days += 1        
    # print(len(fish))
    
    nb = math.floor(256 / 7)
    print(nb * len(fish))

if __name__ == "__main__":
    main(sys.argv[1:])


# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)

# 547116 too high
# 502179 too high