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
    print('provided', input_value)
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
        if len(return_values) == 3:
            go = False

    return (opcode, return_values)
    # result = input_value

def format_result():
    global result
    # print(result[0])
    # print('shape', result.shape)
    result = [b''.join(result[:,x]) for x in range(result.shape[1])]


def main():
    global input_data, result, relative_base, real_input_data, n
    input_data = input_data.split(',') + [0] * 1000
    input_data[0] = 2
    real_input_data = input_data[:]
    # print(input_data)
    opcode = None
    tiles = []
    score = None
    joystick_positions = ['left', 'center', 'right']
    joystick_position = 'center'

    l = np.chararray((43, 21))
    l[:] = b'.'

    # BUILD THE BOARD
    while not score:
        (opcode, values) = process(0)
        if len(values) == 3 and not values[0] == -1 and not values[1] == 0:
            [x, y, val] = values
            tiles.append(values)
            if val == 0: # empty
                l[x, y-1] = b'.'
            elif val == 1: # wall
                l[x, y-1] = b'|'
            elif val == 2: # block
                l[x, y-1] = b'#'
            elif val == 3: # paddle
                l[x, y-1] = b'_'
            elif val == 4: # ball
                l[x, y-1] = b'o'
            else:
                l[x, y-1] = b'?'
        elif values[0] == -1 and values[1] == 0:
            score = values[2]

    result = l
    format_result()
    ppprint(result)

    # PLAY !
    input_data = real_input_data[:]
    relative_base = 0
    n = 0

    blocks = np.where(l == b'#')

    while opcode != 99:
        # Move joystick
        (ball_x, ball_y) = np.where(l == b'o')
        (padd_x, padd_y) = np.where(l == b'_')
        # print(ball_x, ball_y)
        if len(ball_x) and len(padd_x):
            if ball_x[0] > padd_x[0]:
                joystick_position = 'right'
            elif ball_x[0] < padd_x[0]:
                joystick_position = 'left'
            elif ball_x[0] == padd_x[0]:
                joystick_position = 'center'
        # else:
            # joystick_position = 'center'
            # do nothing

        print(n, joystick_position, ball_x, ball_y, padd_x, padd_y)

        (opcode, values) = process(joystick_positions.index(joystick_position)-1)
        if opcode == 99:
            continue
        [x, y, val] = values
        if len(values) == 3 and not x == -1 and not y == 0:
            if val == 0: # empty
                l[x, y-1] = b'.'
            elif val == 1: # wall
                l[x, y-1] = b'|'
            elif val == 2: # block
                l[x, y-1] = b'#'
            elif val == 3: # paddle
                l[x, y-1] = b'_'
            elif val == 4: # ball
                l[x, y-1] = b'o'
            else:
                l[x, y-1] = b'?'
        elif x == -1 and y == 0:
            score = val
            blocks = np.where(l == b'#')
            if len(blocks[0]) == 0:
                joystick_position = 'center'
                print('NO TILES LEFT')
            print('SCORE', score)
        # n += 1
        result = l
        # format_result()
        # ppprint(result)
        # print(x, y, val)



    result = l
    format_result()
    print('SCORE', score)

if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)


# 14186 too low
# 14200 too low
