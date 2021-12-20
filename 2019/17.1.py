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
# input_file = path.splitext(path.basename(__file__))[0] + '.test.txt'
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

def process(input_value = None):
    global input_data, result, relative_base, n
    go = True
    # 0 = position mode
    # 1 = immediate mode
    # 2 = relative mode
    # print('input', input_value)
    iteration = 0
    return_values = []
    # print('length', len(input_data))
    while go:
        try:
            inst = '0000' + str(input_data[n])
            inst = inst[-5:]
            opcode = int(inst[-2:])
            mode_p1 = int(inst[-3:-2])
            mode_p2 = int(inst[-4:-3])
            mode_p3 = int(inst[-5:-4])
            # print(opcode, mode_p1, mode_p2, mode_p3)
            # print(opcode)

            if opcode == 1:
                val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[relative_base + int(input_data[n+1])]) if mode_p1 == 2 else int(input_data[int(input_data[n+1])])
                val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[relative_base + int(input_data[n+2])]) if mode_p2 == 2 else int(input_data[int(input_data[n+2])])
                if mode_p3 == 1:
                    input_data[n+3] = val1 + val2
                elif mode_p3 == 2:
                    input_data[relative_base + int(input_data[n+3])] = val1 + val2
                else:
                    input_data[int(input_data[n+3])] = val1 + val2
                # print(opcode, val1, val2)
                n += 4
            elif opcode == 2:
                val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[relative_base + int(input_data[n+1])]) if mode_p1 == 2 else int(input_data[int(input_data[n+1])])
                val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[relative_base + int(input_data[n+2])]) if mode_p2 == 2 else int(input_data[int(input_data[n+2])])
                if mode_p3 == 1:
                    input_data[n+3] = val1 * val2
                elif mode_p3 == 2:
                    input_data[relative_base + int(input_data[n+3])] = val1 * val2
                else:
                    input_data[int(input_data[n+3])] = val1 * val2
                # print(opcode, val1, val2)
                # print(iteration, n, opcode, inst, val1, val2)
                n += 4
            elif opcode == 3:
                if mode_p1 == 0:
                    input_data[int(input_data[n+1])] = input_value
                elif mode_p1 == 2:
                    input_data[relative_base + int(input_data[n+1])] = input_value
                # print(opcode, input_value)
                # print(iteration, n, inst)
                n += 2
            elif opcode == 4:
                input_value = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[relative_base + int(input_data[n+1])]) if mode_p1 == 2 else int(input_data[int(input_data[n+1])])
                # return_values.append(input_value)
                # print('output', input_value)
                n += 2
                yield input_value
                # print(opcode, input_value)
                # print('-->', input_value)
            elif opcode == 5:
                # print(input_data[n+1], relative_base, input_data[relative_base + int(input_data[n+1])], input_data[int(input_data[n+1])])
                val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[relative_base + int(input_data[n+1])]) if mode_p1 == 2 else int(input_data[int(input_data[n+1])])
                val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[relative_base + int(input_data[n+2])]) if mode_p2 == 2 else int(input_data[int(input_data[n+2])])
                # print(iteration, n, opcode, inst, val1, val2)
                n = val2 if val1 != 0 else n+3
                # print(opcode, val1, val2)
            elif opcode == 6:
                val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[relative_base + int(input_data[n+1])]) if mode_p1 == 2 else int(input_data[int(input_data[n+1])])
                val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[relative_base + int(input_data[n+2])]) if mode_p2 == 2 else int(input_data[int(input_data[n+2])])
                # print(6, val1, val2)
                # print(iteration, n, opcode, inst, val1, val2)
                n = val2 if val1 == 0 else n+3
                # print(opcode, val1, val2)
            elif opcode == 7:
                val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[relative_base + int(input_data[n+1])]) if mode_p1 == 2 else int(input_data[int(input_data[n+1])])
                val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[relative_base + int(input_data[n+2])]) if mode_p2 == 2 else int(input_data[int(input_data[n+2])])
                pos3 = relative_base + int(input_data[n+3]) if mode_p3 == 2 else int(input_data[n+3])
                input_data[pos3] = 1 if val1 < val2 else 0
                # print(iteration, n, opcode, inst, val1, val2)
                n += 4
                # print(opcode, val1, val2)
            elif opcode == 8:
                val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[relative_base + int(input_data[n+1])]) if mode_p1 == 2 else int(input_data[int(input_data[n+1])])
                val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[relative_base + int(input_data[n+2])]) if mode_p2 == 2 else int(input_data[int(input_data[n+2])])
                pos3 = relative_base + int(input_data[n+3]) if mode_p3 == 2 else int(input_data[n+3])
                input_data[pos3] = 1 if val1 == val2 else 0
                # print(iteration, n, opcode, inst, val1, val2)
                n += 4
            elif opcode == 9:
                # val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[int(input_data[n+1])])
                val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[relative_base + int(input_data[n+1])]) if mode_p1 == 2 else int(input_data[int(input_data[n+1])])
                # print(opcode, relative_base, relative_base+val1)
                relative_base += (val1)
                # print(opcode, relative_base)
                n += 2

            else:
                print('--->', opcode)
                go = False
            iteration += 1
        except Exception as e:
            print('error', opcode)
            raise e
        # if len(return_values) == 3:
        #     print('---->', opcode)
        #     go = False

    return (opcode, return_values)
    # result = input_value


def main():
    global input_data, result
    input_data = input_data.split(',') + [0] * 10000
    # print(input_data)
    # table = np.zeros((0,0))
    table = [[]]
    print(table)
    gen = process()
    for val in gen:
        # val = next(gen)
        if val == 46: # .
            # np.append(table, '.', axis = 1)
            table[len(table)-1].append('.')
        elif val == 35: # #
            # np.append(table, '#', axis = 1)
            table[len(table)-1].append('#')
        elif val == 10: # new line
            # np.append(table, [], axis = 0)
            table.append([])
    result = table

    # ppprint(table)
    # [[print(x, y) for y,_ in enumerate(row)] for x,row in enumerate(table)]
    # sum_inter = sum([sum([x*y if (table[x][y] == '#' and (x > 0 and table[x-1][y] == '#') and (x < len(table)-1 and table[x+1][y] == '#') and (y > 0 and table[x][y-1] == '#') and (y < len(table[x])-1 and table[x][y+1] == '#')) else 0 for y,_ in enumerate(row)]) for x,row in enumerate(table)])
    # sum_inter = [[print(x,y) for y,_ in enumerate(row)] for x,row in enumerate(table)]
    # print(sum_inter)

    res = 0
    # print(len(table), len(table[0]))
    # exit()
    for x in range(len(table)):
        for y in range(len(table[x])):
            print(len(table)-1, x+1, x,y)
            if table[x][y] == '#' \
                and (x > 0 and table[x-1][y] == '#')  \
                and (x < len(table)-1 and len(table[x+1]) >= y-1 and table[x+1][y] == '#')  \
                and (y > 0 and table[x][y-1] == '#') \
                and (y < len(table[x])-1 and table[x][y+1] == '#'):
                res += x*y

    print(res)
    format_result()


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
