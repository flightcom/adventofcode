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
import random
import sys

np.set_printoptions(threshold=sys.maxsize)
np.core.arrayprint._line_width = 200
np.set_printoptions(edgeitems=100, linewidth=200, 
    formatter=dict(float=lambda x: "%.3g" % x))

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
                return_values.append(input_value)
                # print('output', input_value)
                n += 2
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
        if len(return_values) == 1:
            go = False

    # print(opcode, return_values)
    return (opcode, return_values)
    # result = input_value

def format_result():
    global result
    result = [b''.join(result[:,x]) for x in range(result.shape[1])]


def add_extra_column(table, before = False, after = False):
    col = np.zeros((table.shape[0], 1))
    if before:
        table = np.append(col, table, axis=1)
    if after:
        table = np.append(table, col, axis=1)
    return table


def add_extra_row(table, before = False, after = False):
    row = np.zeros((1, table.shape[1]))
    if before:
        table = np.append(row, table, axis=0)
    if after:
        table = np.append(table, row, axis=0)
    return table

def get_next_direction(current_direction):
    new_direction = random.randrange(1, 5, 1)
    # if current_direction == 1:
    #     return 4
    # elif current_direction == 2:
    #     return 3
    # elif current_direction == 3:
    #     return 1
    # else:
    #     return 2
    if new_direction == current_direction:
        return get_next_direction(current_direction)
    else:
        return new_direction


def main():
    global input_data, result
    input_data = input_data.split(',') + [0] * 1000

    go = True

    table = np.ones((1, 1))
    position = (0,0)
    table[position] = 9
    direction = 1

    moves = []

    while go:
        if position[0] == 0 and direction == 1:  # NORTH
            table = add_extra_row(table, before = True)
            position = (position[0]+1, position[1])
        elif position[0] == table.shape[0] - 1 and direction == 2:  # SOUTH
            table = add_extra_row(table, after = True)
        elif position[1] == 0 and direction == 3: # WEST
            table = add_extra_column(table, before = True)
            position = (position[0], position[1]+1)
        elif position[1] == table.shape[1] - 1 and direction == 4: # EAST
            table = add_extra_column(table, after = True)

        if direction == 1:
            next_position = (position[0]-1, position[1])
        elif direction == 2:
            next_position = (position[0]+1, position[1])
        elif direction == 3:
            next_position = (position[0], position[1]-1)
        else:
            next_position = (position[0], position[1]+1)

        # print(position, direction, table.shape)
        # print(table)

        # if table[next_position] == 1 or table[next_position] == 9:
        #     position = next_position[:]
        #     direction = get_next_direction(direction)
        #     continue
        # elif table[next_position] == 8:
        #     direction = get_next_direction(direction)

        nex = process(direction)
        # print('nex', nex)
        if nex[0] == 99:
            go = False
            continue
    
        val = nex[1][0]
        # print(position, next_position, nex[1])

        if val == 0:
            table[next_position] = 8
            # direction = get_next_direction(direction)
        elif val == 1:
            position = next_position[:]
            moves.append(direction)
            table[position] = 1 if table[position] != 9 else 9
        elif val == 2:
            table[position] = 2
            go = False

        direction = get_next_direction(direction)

    print(table)
    origin = np.where(table == 9)
    dest = np.where(table == 2)
    print(origin, dest, abs(dest[1]-origin[1]) + abs(dest[0]-origin[0]))

    go = True
    while go:
        found = False
        for i, m in enumerate(moves):
            if i < len(moves) -2:
                if m == 1 and moves[i+1] == 2 or m == 2 and moves[i+1] == 1:
                    moves[i] = 0
                    moves[i+1] = 0
                    found = True
                if m == 3 and moves[i+1] == 4 or m == 4 and moves[i+1] == 3:
                    moves[i] = 0
                    moves[i+1] = 0
                    found = True
        moves = [m for m in moves if m != 0]
        if not found:
            go = False
        print(len(moves))
        
    print(moves, len(moves))

    # print(origin, dest, np.linalg.norm(dest-origin))

if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)


# 116 too low
# 130 too low
# 151 too low