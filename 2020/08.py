# IMPORTS
from os import path
from scipy import stats
import math
import numpy as np
import pprint
import re
import copy
# import matplotlib.pyplot as plt
from numpy import unravel_index
import sys, getopt
import operator

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

def part1():
    global input_data, result
    acc = 0
    instructions_executed = []
    cont = True
    i = 0
    while cont:
        [ins, value] = input_data[i].split()
        print(i, ins, value)
        instructions_executed.append(i)
        if ins == 'jmp':
            i = eval('{} + {} - 1'.format(i, value))
        elif ins == 'acc':
            acc = eval('{} + {}'.format(acc, value))
        i += 1

        if i in instructions_executed:
            cont = False
            continue

    result = acc

def part2():
    global input_data, result
    instructions_executed = []
    tried_changing = []
    cont = True
    found = False
    i = 0

    looping_count = 0

    # count lines matching jmp or acc
    count = 0
    for line in input_data:
        if not re.match('^acc', line):
            count += 1

    print(count)

    while len(tried_changing) < count and not found:

        instructions_executed = []
        i = 0
        acc = 0

        input_data_copy = copy.copy(input_data)
        cont = True
        for j in range(len(input_data)):
            if j not in tried_changing:
                if re.match('jmp', input_data_copy[j]):
                    print(j, 'changing jmp to nop')
                    input_data_copy[j] = input_data_copy[j].replace('jmp', 'nop')
                    tried_changing.append(j)
                    break
                elif re.match('nop', input_data_copy[j]):
                    print(j, 'changing nop to jmp')
                    input_data_copy[j] = input_data_copy[j].replace('nop', 'jmp')
                    tried_changing.append(j)
                    break

        while cont:
            [ins, value] = input_data_copy[i].split()
            print(i, ins, value, acc)
            instructions_executed.append(i)

            if ins == 'jmp':
                i = eval('{} + {} - 1'.format(i, value))
            elif ins == 'acc':
                acc = eval('{} + {}'.format(acc, value))

            if i == len(input_data_copy) - 1:
                print('END REACHED !')
                cont = False
                found = True

            i += 1

            if i in instructions_executed:
                print('LOOPING')
                looping_count += 1
                cont = False
                continue

        # if not cont:
        #     break

    result = acc



if __name__ == "__main__":
    main(sys.argv[1:])


# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)


# between 43316 and 50000