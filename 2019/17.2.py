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


def process(input_values = None):
    global input_data, result, relative_base, n
    print('input', input_values)
    go = True
    # 0 = position mode
    # 1 = immediate mode
    # 2 = relative mode
    iteration = 0
    return_values = []
    if input_values:
        print('YES')
        input_values = input_values.reverse()
    # print('length', len(input_data))
    while go:
        try:
            inst = '0000' + str(input_data[n])
            inst = inst[-5:]
            # print(n, iteration, inst)
            opcode = int(inst[-2:])
            mode_p1 = int(inst[-3:-2])
            mode_p2 = int(inst[-4:-3])
            mode_p3 = int(inst[-5:-4])
            # print(opcode, mode_p1, mode_p2, mode_p3)
            if input_values:
                print(opcode)

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
                print('using', input_values[-1])
                if mode_p1 == 0:
                    input_data[int(input_data[n+1])] = input_values[-1]
                elif mode_p1 == 2:
                    input_data[relative_base + int(input_data[n+1])] = input_values[-1]
                input_values.pop()
                # print(opcode, input_value)
                # print(iteration, n, inst)
                n += 2
            elif opcode == 4:
                if input_values:
                    print('-----------> YES')
                ret = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[relative_base + int(input_data[n+1])]) if mode_p1 == 2 else int(input_data[int(input_data[n+1])])
                # input_values.append(int(input_data[n+1]) if mode_p1 == 1 else int(input_data[relative_base + int(input_data[n+1])]) if mode_p1 == 2 else int(input_data[int(input_data[n+1])]))
                return_values.append(ret)
                # print('output', input_value)
                n += 2
                # yield input_values[-1]
                # print('ret', ret)
                # if not input_values:
                #     yield ret
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
                # print('--->', opcode)
                go = False
            iteration += 1
        except Exception as e:
            print('error', opcode)
            raise e
        # if len(return_values) == 3:
        #     print('---->', opcode)
        #     go = False

    # print('ret', return_values)
    return (opcode, return_values)

def path_to_ascii(path):
    _ascii = []
    reg = r'\w\d+'
    match = re.findall(reg, path)
    for m in match:
        letter = m[0]
        number = int(m[1:])
        if letter == 'L':
            _ascii.append(76)
        elif letter == 'R':
            _ascii.append(82)
        elif letter == 'A':
            _ascii.append(65)
        elif letter == 'B':
            _ascii.append(66)
        elif letter == 'C':
            _ascii.append(67)
        _ascii.append(44)
        if number == 4:
            _ascii.append(52)
        elif number == 6:
            _ascii.append(54)
        elif number == 8:
            _ascii.append(56)
        elif number == 10:
            _ascii.append(58)
        _ascii.append(44)
    _ascii = _ascii[:-1]
    _ascii.append(10)
    return _ascii       

def main():
    global input_data, result, n, relative_base, real_input_data

    input_data = input_data.split(',') + [0] * 10000
    real_input_data = input_data[:]

    gen = process(None)

    table = [[]]
    # print(table)
    for val in gen:
        if val == 46: # .
            table[len(table)-1].append('.')
        elif val == 35: # #
            table[len(table)-1].append('#')
        elif val == 10: # new line
            table.append([])
        elif val == 60: # <
            table[len(table)-1].append('<')
        elif val == 62: # >
            table[len(table)-1].append('>')
        elif val == 94: # ^
            table[len(table)-1].append('^')
        elif val == 118: # v
            table[len(table)-1].append('v')
        # ^, v, <, or >

    result = table

    print('-----------')
    input_data = real_input_data[:]
    relative_base = 0
    n = 0

    input_data[0] = 2

    path = [
        "L8R10L10",
        "R10L8L8L10",
        "L4L6L8L8"
    ]
    final_position = (24, 38)

    routine = ['A','B','A','C','B','C','A','C','B','C']
    routine = [65, 44, 66, 44, 65, 44, 65, 44, 65, 44, 65, 44, 65, 44, 65, 44, 65, 44, 65, 44, 10]

    path = [path_to_ascii(p) for p in path]

    # inputs = inputs + path + [[121, 10]]
    inputs = [routine] + path
    ppprint(inputs)
    # exit()

    vals = []
    for i in inputs:
        n = 0
        relative_base = 0
        input_data = real_input_data[:]
        print('testing', i)
        process(i)
        vals.append(gen)

    for v in vals:
        for w in v:
            print('test', w)


    # format_result()


def format_result():
    global result
    result = [''.join(result[x]) for x in range(len(result))]


if __name__ == "__main__":
    main()

# OUTPUT RESULT
# try:
#     result
# except NameError:
#     print("Result is not defined")
# else:
#     ppprint(result)

#.......#.#.......................#...#

# ABCBC

# L8R10L10R10L8L8L10
# L8R10L10L4L6L8L8R10
# L8L8L10L4L6L8L8
# L8R10L10L4L6L8L8R10
# L8L8L10L4L6L8L8


# L8R10L10R10L8L8L10L8R10L10L4L6L8L8R10L8L8L10L4L6L8L8L8R10L10L4L6L8L8R10L8L8L10L4L6L8L8
# L8R10L10L4L6L8L8R10
# L8L8L10L4L6L8L8
# L8R10L10L4L6L8L8R10
# L8L8L10L4L6L8L8