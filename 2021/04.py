# IMPORTS
from os import path
# from scipy import stats
import math
# import numpy as np
import pprint
import re
import copy
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
def create_combined_matrices():
    global input_data
    combined_matrices = []
    matrix = []
    bool_matrix = [
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
    ]
    for line in input_data:
        if len(line.split(',')) > 1:
            continue
        if line == '':
            if matrix != []:
                combined_matrices.append((matrix, copy.deepcopy(bool_matrix)))            
            matrix = []
        else:
            values = line.split()
            values = [int(x) for x in values]
            matrix.append(values)
    return combined_matrices

def check_matrix_col(combined_matrix):
    val_matrix = combined_matrix[0]
    bool_matrix = combined_matrix[1]
    for i in range(len(bool_matrix[0])):
        for j in range(len(bool_matrix[0])):
            if bool_matrix[j][i] == False:
                break
            else:
                if j == len(bool_matrix[0]) -1:
                    return True
    return False
        
def check_matrix_row(combined_matrix):
    val_matrix = combined_matrix[0]
    bool_matrix = combined_matrix[1]
    for i in range(len(bool_matrix[0])):
        for j in range(len(bool_matrix[0])):
            if bool_matrix[i][j] == False:
                break
            else:
                if j == len(bool_matrix[0]) -1:
                    return True
    return False


def check_matrices(combined_matrices: list, n: int):
    for cm in combined_matrices:
        val_matrix = cm[0]
        bool_matrix = cm[1]
        for i in range(len(bool_matrix[0])):
            for j in range(len(bool_matrix[0])):
                if val_matrix[i][j] == n:
                    bool_matrix[i][j] = True        

def get_sum_unmarked(cm):
    val_matrix = cm[0]
    bool_matrix = cm[1]
    sum_false = 0
    for i in range(len(bool_matrix[0])):
        for j in range(len(bool_matrix[0])):
            if bool_matrix[i][j] == False:
                sum_false += val_matrix[i][j]
    return sum_false


def part1():
    global input_data, result
    combined_matrices = create_combined_matrices()
    numbers = input_data[0].split(',')
    for n in numbers:
        n = int(n)
        check_matrices(combined_matrices, n)
        for cm in combined_matrices:
            res_row = check_matrix_row(cm)
            res_col = check_matrix_col(cm)
            if res_row or res_col:
                result = get_sum_unmarked(cm) * n
                return
    return

def part2():
    global input_data, result
    combined_matrices = create_combined_matrices()
    numbers = input_data[0].split(',')
    for n in numbers:
        n = int(n)
        check_matrices(combined_matrices, n)
        print(len(combined_matrices))
        for pos, cm in enumerate(combined_matrices):
            res_row = check_matrix_row(cm)
            res_col = check_matrix_col(cm)
            if res_row or res_col:
                result = get_sum_unmarked(cm) * n
                combined_matrices.pop(pos)
                print('we have a result', result, get_sum_unmarked(cm), n)
                print(cm)
                continue
    return

if __name__ == "__main__":
    main(sys.argv[1:])

        

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)

