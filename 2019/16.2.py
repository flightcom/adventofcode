# IMPORTS
from os import path
from scipy import stats
import math
import numpy as np
import pprint
import re
# import matplotlib.pyplot as plt
from numpy import unravel_index
import turtle

# SETUP
input_file = path.splitext(path.basename(__file__))[0].split('.')[0] + '.txt'
input_file = path.splitext(path.basename(__file__))[0] + '.test.txt'
# input_file = 'test.txt'
if not path.isfile(input_file):
    input_file = '1.txt'

with open(input_file) as f:
    input_data = f.read()
# with open(input_file) as f:
#     input_data = f.read().split()
# with open(input_file) as f:
#     input_data = f.read().splitlines()


if not input_data:
    raise Exception('No content !')

# GLOBAL VARIABLES
result = 0
split_data = None
real_input_data = None
relative_base = 0
n = 0

# FUNCTIONS
def ppprint(message, file=None):
    # np.set_printoptions(threshold=np.nan)
    pp = pprint.PrettyPrinter(indent=4, stream=file, width=150)
    pp.pprint(message)


def draw(X, Y):
    plt.plot(X, Y, 'ro')
    # Reverse Y-Axis
    plt.gca().invert_yaxis()
    plt.show()

# SOLUTION GOES HERE
base_pattern = [0, 1, 0, -1]

def get_base_pattern(nb: int):
    global base_pattern
    return list(np.repeat(base_pattern, nb))


def main():
    global input_data, result
    # print(input_data)
    coef = 10000
    input_data = list(input_data * coef)
    # print('start', input_data[:10])
    input_data = np.array(input_data)
    # print('done', input_data.size)
    # exit()
    my_input = input_data
    patterns = {n: get_base_pattern(n+1) * (math.ceil(len(my_input)/len(base_pattern))+1) for n in range(len(my_input))[:len(my_input)]}
    print('done with patterns')
    exit()

    loops = 100
    # for l in range(loops):
    #     temp = []
    #     for n in range(len(my_input)):
    #         pattern = get_base_pattern(n+1) * (math.ceil(len(input_data)/len(base_pattern))+1)
    #         res = sum([int(inp) * int(pattern[i+1]) for i, inp in enumerate(my_input)])
    #         temp.append(str(res)[-1])
    #     my_input = ''.join(temp)
    #     print(l, '------->', my_input)
    for l in range(loops):
        my_input = ''.join([str(sum([int(inp) * int((get_base_pattern(n+1) * (math.ceil(len(input_data)/len(base_pattern))+1))[i+1]) for i, inp in enumerate(my_input)]))[-1] for n in range(len(my_input))])
        print(l, '------->', my_input)
    # result = int(my_input[:8])
    result = int(my_input[input_data:])



if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)


# 24176176
# 93300860 too high