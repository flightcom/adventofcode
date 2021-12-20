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
# input_file = path.splitext(path.basename(__file__))[0] + '.test.txt'
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

def pre():
    global input_data
    # replace position 1 with the value 12 and replace position 2 with the value 2
    input_data[1] = 12
    input_data[2] = 2

def pre2(v1, v2):
    global input_data
    input_data[1] = v1
    input_data[2] = v2

def split():
    global input_data, split_data
    split_data = []
    n = 0
    while n < len(input_data):
        if input_data[n] != 99:
            l = 4
        else:
            l = 1
        split_data.append(input_data[n:n+l])
        n += l

def process(inp):
    global input_data, result
    go = True
    n = 0
    # 0 = position mode
    # 1 = immediate mode
    input_value = inp
    iteration = 0
    print(len(input_data))
    while go:
        inst = '0000' + str(input_data[n])
        inst = inst[-5:]
        opcode = int(inst[-2:])
        mode_p1 = int(inst[-3:-2])
        mode_p2 = int(inst[-4:-3])
        mode_p3 = int(inst[-5:-4])
        # print(opcode, mode_p1, mode_p2, mode_p3)

        if opcode == 1:
            val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[int(input_data[n+1])])
            val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[int(input_data[n+2])])
            if mode_p3 == 1:
                input_data[n+3] = val1 + val2
            else:
                input_data[int(input_data[n+3])] = val1 + val2
            print(iteration, n, opcode, inst, val1, val2)
            n += 4
        elif opcode == 2:
            val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[int(input_data[n+1])])
            val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[int(input_data[n+2])])
            if mode_p3 == 1:
                input_data[n+3] = val1 * val2
            else:
                input_data[int(input_data[n+3])] = val1 * val2
            print(iteration, n, opcode, inst, val1, val2)
            n += 4
        elif opcode == 3:
            input_data[int(input_data[n+1])] = input_value
            print(iteration, n, inst)
            n += 2
        elif opcode == 4:
            input_value = input_data[int(input_data[n+1])]
            # print('output', input_value)
            print(iteration, n, opcode, inst, input_value)
            n += 2
        elif opcode == 5:
            val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[int(input_data[n+1])])
            val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[int(input_data[n+2])])
            # print(5, val1, val2)
            print(iteration, n, opcode, inst, val1, val2)
            n = val2 if val1 != 0 else n+3
        elif opcode == 6:
            val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[int(input_data[n+1])])
            val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[int(input_data[n+2])])
            # print(6, val1, val2)
            print(iteration, n, opcode, inst, val1, val2)
            n = val2 if val1 == 0 else n+3
        elif opcode == 7:
            val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[int(input_data[n+1])])
            val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[int(input_data[n+2])])
            # pos3 = int(input_data[n+3]) if mode_p2 == 1 else int(input_data[int(input_data[n+3])])
            pos3 = int(input_data[n+3])
            input_data[pos3] = 1 if val1 < val2 else 0
            print(iteration, n, opcode, inst, val1, val2)
            n += 4
        elif opcode == 8:
            val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[int(input_data[n+1])])
            val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[int(input_data[n+2])])
            # pos3 = int(input_data[n+3]) if mode_p2 == 1 else int(input_data[int(input_data[n+3])])
            pos3 = int(input_data[n+3])
            input_data[pos3] = 1 if val1 == val2 else 0
            print(iteration, n, opcode, inst, val1, val2)
            n += 4

        else:
            print(iteration, n, inst)
            go = False
        iteration += 1

    # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    # Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    # Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.


    result = input_value


def main():
    global input_data, result
    input_data = input_data.split(',')
    # print(input_data)
    process(5)

def main2():
    global input_data, result, real_input_data
    input_data = input_data.split(',')
    input_data = [int(x) for x in input_data]
    real_input_data = input_data[:]
    inp1 = 0
    inp2 = 0
    for i in range(99):
        for j in range(99):
            run(i, j)
            if result == 19690720:
                ppprint('STOP')
                ppprint(100 * i + j)


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


# 5496377 too high
# 5463605 too high