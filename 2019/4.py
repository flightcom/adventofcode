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
input_file = path.splitext(path.basename(__file__))[0] + '.txt'
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
    result = []
    (start, end) = input_data.split('-')
    print(start, end)
    for password in range(int(start), int(end)):
        password = str(password)
        # print(password)
        has_double = 0
        has_triple = 0
        has_quadruple = 0
        has_quintuple = 0
        has_sixtuple = 0
        has_lower = 0
        for num, l in enumerate(password):
            l = int(l) 
            if num > 0:
                if l < int(password[num -1]):
                    has_lower = True
            if num > 4 and l == int(password[num -1]) and l == int(password[num -2]) and l == int(password[num -3]) and l == int(password[num -4]) and l == int(password[num -5]):
                has_sixtuple += 1
                has_quintuple -= 1
            elif num > 3 and l == int(password[num -1]) and l == int(password[num -2]) and l == int(password[num -3]) and l == int(password[num -4]):
                has_quintuple += 1
                has_quadruple -= 1
            elif num > 2 and l == int(password[num -1]) and l == int(password[num -2]) and l == int(password[num -3]):
                has_quadruple += 1
                has_triple -= 1
            elif num > 1 and l == int(password[num -1]) and l == int(password[num -2]):
                has_triple += 1
                has_double -= 1
            elif num > 0 and l == int(password[num -1]):
                has_double += 1
        if has_double > 0 and not has_lower:
            result.append(password)
        # else:
        #     continue
        # break
            
    result = len(result)

def main2():
    global input_data, result


if __name__ == "__main__":
    main()
    # main2()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
