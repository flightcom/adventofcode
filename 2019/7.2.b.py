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

result = 0
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

def process(inp, phase):
    global input_data, result, real_input_data
    input_data = real_input_data[:]
    go = True
    n = 0
    # 0 = position mode
    # 1 = immediate mode
    input_value = phase
    iteration = 0
    while go:
        try:
            if iteration == 1:
                input_value = inp
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
                # print(iteration, n, opcode, inst, val1, val2)
                n += 4
            elif opcode == 2:
                val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[int(input_data[n+1])])
                val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[int(input_data[n+2])])
                if mode_p3 == 1:
                    input_data[n+3] = val1 * val2
                else:
                    input_data[int(input_data[n+3])] = val1 * val2
                # print(iteration, n, opcode, inst, val1, val2)
                n += 4
            elif opcode == 3:
                input_data[int(input_data[n+1])] = input_value
                # print(iteration, n, inst)
                n += 2
            elif opcode == 4:
                input_value = input_data[int(input_data[n+1])]
                # print(iteration, n, opcode, inst, input_value)
                n += 2
            elif opcode == 5:
                val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[int(input_data[n+1])])
                val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[int(input_data[n+2])])
                # print(iteration, n, opcode, inst, val1, val2)
                n = val2 if val1 != 0 else n+3
            elif opcode == 6:
                val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[int(input_data[n+1])])
                val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[int(input_data[n+2])])
                # print(iteration, n, opcode, inst, val1, val2)
                n = val2 if val1 == 0 else n+3
            elif opcode == 7:
                val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[int(input_data[n+1])])
                val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[int(input_data[n+2])])
                pos3 = int(input_data[n+3])
                input_data[pos3] = 1 if val1 < val2 else 0
                # print(iteration, n, opcode, inst, val1, val2)
                n += 4
            elif opcode == 8:
                val1 = int(input_data[n+1]) if mode_p1 == 1 else int(input_data[int(input_data[n+1])])
                val2 = int(input_data[n+2]) if mode_p2 == 1 else int(input_data[int(input_data[n+2])])
                pos3 = int(input_data[n+3])
                input_data[pos3] = 1 if val1 == val2 else 0
                # print(iteration, n, opcode, inst, val1, val2)
                n += 4

            else:
                # print(iteration, n, inst)
                go = False
            iteration += 1
        except Exception as e:
            print('error', e)
            raise e

    return input_value

def main():
    global input_data, result, real_input_data
    input_data = input_data.split(',')
    real_input_data = input_data[:]
    result = 0
    best_phase_setting = None
    phase_settings = {}
    print(input_data)
    amp1 = None
    amp2 = None
    amp3 = None
    amp4 = None
    amp5 = None
    count = 0
    phase_range = range(5, 10)
    for i1 in range(5):
        # print('i1', i1)
        phase_settings[5] = None
        phase_settings[3] = None
        phase_settings[4] = None
        phase_settings[2] = None
        phase_settings[1] = i1
        for i2 in [x for x in phase_range if x not in phase_settings.values()]:
            # print('i2', i2)
            phase_settings[5] = None
            phase_settings[3] = None
            phase_settings[4] = None
            phase_settings[2] = i2
            for i3 in [x for x in phase_range if x not in phase_settings.values()]:
                # print('i3', i3)
                phase_settings[5] = None
                phase_settings[4] = None
                phase_settings[3] = i3
                for i4 in [x for x in phase_range if x not in phase_settings.values()]:
                    # print('i4', i4)
                    phase_settings[5] = None
                    phase_settings[4] = i4
                    for i5 in [x for x in phase_range if x not in phase_settings.values()]:
                        # print('i5', i5)
                        phase_settings[5] = i5
                        # print(phase_settings)
                        # print(phase_settings.values())
                        count += 1
                        try:
                            # print('Processing AMP 1')
                            amp_1 = process(0, i1)
                            # print('Processing AMP 2')
                            amp_2 = process(amp_1, i2)
                            # print('Processing AMP 3')
                            amp_3 = process(amp_2, i3)
                            # print('Processing AMP 4')
                            amp_4 = process(amp_3, i4)
                            # print('Processing AMP 5')
                            amp_5 = process(amp_4, i5)
                            if amp_5 > result:
                                print('setting result to', amp_5)
                                result = amp_5
                                best_phase_setting = str(phase_settings[1])+str(phase_settings[2])+str(phase_settings[3])+str(phase_settings[4])+str(phase_settings[5])
                        except Exception as e:
                            continue
    print('count', count)
    print('best_phase_setting', best_phase_setting)


if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)


# result : 440880