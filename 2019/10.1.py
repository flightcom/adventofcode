# IMPORTS
from os import path
from scipy import stats
import math
import numpy as np
import pprint
import sys
import re
# import matplotlib.pyplot as plt
from numpy import unravel_index
# np.set_printoptions(threshold=np.nan)
np.set_printoptions(threshold=sys.maxsize)

# SETUP
input_file = path.splitext(path.basename(__file__))[0].split('.')[0] + '.txt'
# input_file = path.splitext(path.basename(__file__))[0] + '.test.txt'

# with open(input_file) as f:
#     input_data = f.read()
with open(input_file) as f:
    input_data = f.read().split()
# input_data = np.loadtxt(input_file, dtype=np.object)

if not input_data:
    raise Exception('No content !')

# GLOBAL VARIABLES
result = None

# FUNCTIONS
def ppprint(message, file=None):
    # np.set_printoptions(threshold=np.nan)
    pp = pprint.PrettyPrinter(indent=4, stream=file, width=250)
    pp.pprint(message)


def draw(X, Y):
    plt.plot(X, Y, 'ro')
    # Reverse Y-Axis
    plt.gca().invert_yaxis()
    plt.show()

# SOLUTION GOES HERE
def is_prime(a):
    return all(a % i for i in range(2, a))

def is_b_visible_by_a(a, b):
    global input_data
    # x = horizontal
    # y = vertical
    diff_x = abs(b[0] - a[0])
    diff_y = abs(b[1] - a[1])

    # If same points
    # if a[0] == b[0] and a[1] == b[1]:
    if a == b:
        return 0

    if input_data[b[0]][b[1]] != '#':
        return 0

    # Case 1 : exactly 1 row/column between : always true
    if diff_x == 1 or diff_y == 1:
        # print('ok for', b, diff_x, diff_y, b[0] - a[0], b[1] - a[1])
        return 1

    if diff_x == diff_y and diff_x >= 2:
        for i in range(1, diff_x):
            if b[0] > a[0]:
                x = a[0]+i
            else:
                x = a[0]-i
            if b[1] > a[1]:
                y = a[1]+i
            else:
                y = a[1]-i
            if input_data[x][y] == '#':
                # print('something at', x, y)
                return 0

    # Case 2 : same row/column
    if diff_x == 0:
        list_between = [1 if input_data[a[0]][min(a[1],b[1])+y] == '#' else 0 for y in range(1,abs(b[1]-a[1]))]
        # print(list_between)
        is_something_between = sum(list_between) > 0
        if not is_something_between:
            # print('ok for', b, diff_x, diff_y, b[0] - a[0], b[1] - a[1])
            return 1
        else:
            return 0
    elif diff_y == 0:
        list_between = [1 if input_data[min(a[0],b[0])+x][a[1]] == '#' else 0 for x in range(1,abs(b[0]-a[0]))]
        # print(list_between)
        is_something_between = sum(list_between) > 0
        if not is_something_between:
            # print('ok for', b, diff_x, diff_y, b[0] - a[0], b[1] - a[1])
            return 1
        else:
            return 0

    # if is_prime(diff_x) or is_prime(diff_y):
    #     return 1

    # # Case 3 : diff x/y not divisible by diff y/x
    # if not (max(diff_x, diff_y)/max(diff_x, diff_y)).is_integer():
    #     # print('ok for', b)
    #     return 1

    m = min(diff_x, diff_y)
    M = max(diff_x, diff_y)

    q = M/m
    for i in range(m):
        val = q*i
        print(i, m, M, q, val)
        if not val.is_integer():
            continue 
        if diff_x < diff_y:
            if b[0] > a[0]:
                x = b[0]-i
            else:
                x = b[0]+i
            if b[1] > a[1]:
                y = b[1]-int(val)
            else:
                y = b[1]+int(val)
            diff = (i, int(val))
        else:
            if b[0] > a[0]:
                x = b[0]-int(val)
            else:
                x = b[0]+int(val)
            if b[1] > a[1]:
                y = b[1]-i
            else:
                y = b[1]+i
            diff = (int(val), i)
        if input_data[x][y] == '#':
            return 0


    # cd = get_common_divisors(diff_x, diff_y)
    # if len(cd) > 0:
    #     # print(b, cd, diff_x, diff_y)
    #     for d in cd:
    #         diff = (int(diff_x/d), int(diff_y/d))
    #         if b[0] > a[0]:
    #             x = a[0]+diff[0]
    #         else:
    #             x = a[0]-diff[0]
    #         if b[1] > a[1]:
    #             y = a[1]+diff[1]
    #         else:
    #             y = a[1]-diff[1]
    #         # print(diff, x, y)

    #         if input_data[x][y] == '#':
    #             return 0

    # if max(diff_x, diff_y) % min(diff_x, diff_y) == 0:
    #     # print(max(diff_x, diff_y), 'divisible by', min(diff_x, diff_y), diff_x, diff_y, b)
    #     for i in range(1, min(diff_x, diff_y)):
    #         if diff_x < diff_y:
    #             if b[0] > a[0]:
    #                 x = b[0]-i
    #             else:
    #                 x = b[0]+i
    #             if b[1] > a[1]:
    #                 y = b[1]-int(i*(diff_y/diff_x))
    #             else:
    #                 y = b[1]+int(i*(diff_y/diff_x))
    #             diff = (i, int(i*(diff_y/diff_x)))
    #         else:
    #             if b[0] > a[0]:
    #                 x = b[0]-int(i*(diff_x/diff_y))
    #             else:
    #                 x = b[0]+int(i*(diff_x/diff_y))
    #             if b[1] > a[1]:
    #                 y = b[1]-i
    #             else:
    #                 y = b[1]+i
    #             diff = (int(i*(diff_x/diff_y)), i)
    #         # print(diff, x, y)
    #         if input_data[x][y] == '#':
    #             return 0

    # print('ok for', b, diff_x, diff_y, b[0] - a[0], b[1] - a[1])
    return 1

def ppcm(*n):
    """Calcul du 'Plus Petit Commun Multiple' de n (>=2) valeurs entières (Euclide)"""
    def _pgcd(a,b):
        while b: a, b = b, a%b
        return a
    p = abs(n[0]*n[1])//_pgcd(n[0], n[1])
    for x in n[2:]:
        p = abs(p*x)//_pgcd(p, x)
    return p

def get_max_value_in_2d_list(my_list):
    flattened_list = [y for x in my_list for y in x]
    return max(flattened_list)


def get_common_divisors(a, b):
    my_list = []
    for i in range(2, min(a, b)):
        if a%i==0 and b%i==0:
            my_list.append(i)
    # print('common divisors for', a, b, my_list)
    return my_list


def main():
    global input_data, result
    input_data = [list(s) for s in input_data]
    result = [[0]*len(input_data[0]) for _ in range(len(input_data))] 
    # print(input_data)

    # i for vertical
    for i in range(len(input_data)):
        # j for horizontal
        for j in range(len(input_data[i])):

            a = (i, j)
            if input_data[i][j] == '.':
                continue

            visibility_map = [[is_b_visible_by_a(a, (x, y)) for y in range(len(input_data[x]))] for x in range(len(input_data))]
            total = sum(sum(visibility_map,[]))

            result[i][j] = total

        else:
            continue
        break

    # print(result)
    max_value = get_max_value_in_2d_list(result)
    result = np.array(result)
    position =  np.where(result == max_value)
    result = result.flatten()
    result = np.sort(result)
    print(position, max_value)
    # format_result()
    # result = formatted(result)


def formatted(table):
    return [''.join([str(i) for i in table[x]]) for x in range(len(table))]


def format_result():
    global result
    result = [''.join(result[x]) for x in range(len(result))]



if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)


# not 49
# 377 too high
# not 151
# not 156
# not 170
# not 368
# not 342
# not 358
# not 359
# not 357
# not 360