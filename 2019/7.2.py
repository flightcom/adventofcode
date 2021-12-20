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
real_input_data = {}
n_amps = None
iterations = None

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

def process(amp_num, signal, phase):
    global result, real_input_data, n_amps, iterations
    input_data = real_input_data[amp_num]
    # print(input_data)
    go = True
    n = n_amps[amp_num]
    iteration = iterations[amp_num]
    # 0 = position mode
    # 1 = immediate mode
    # input_value = phase
    opcode = None
    while go:
        try:
            # if iteration == 1:
            #     input_value = signal
            input_value = phase if iteration == 0 else signal
            # print(n)
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
                go = False
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

    real_input_data[amp_num] = input_data[:]
    n_amps[amp_num] = n
    iterations[amp_num] = iteration
    # print(opcode)
    return (input_value, opcode)

def main():
    global input_data, result, real_input_data, n_amps, iterations
    input_data = input_data.split(',')
    real_input_data = input_data[:]

    result = 0
    best_phase_setting = None
    phase_settings = {}
    # print(input_data)
    amp1 = None
    amp2 = None
    amp3 = None
    amp4 = None
    amp5 = None
    count = 0
    phase_range = range(5, 10)
    for i1 in phase_range:
        phase_settings[5] = None
        phase_settings[3] = None
        phase_settings[4] = None
        phase_settings[2] = None
        phase_settings[1] = i1
        for i2 in [x for x in phase_range if x not in phase_settings.values()]:
            phase_settings[5] = None
            phase_settings[3] = None
            phase_settings[4] = None
            phase_settings[2] = i2
            for i3 in [x for x in phase_range if x not in phase_settings.values()]:
                phase_settings[5] = None
                phase_settings[4] = None
                phase_settings[3] = i3
                for i4 in [x for x in phase_range if x not in phase_settings.values()]:
                    phase_settings[5] = None
                    phase_settings[4] = i4
                    for i5 in [x for x in phase_range if x not in phase_settings.values()]:
                        phase_settings[5] = i5
                        count += 1
                        try:
                            print('new loop', str(phase_settings[1])+str(phase_settings[2])+str(phase_settings[3])+str(phase_settings[4])+str(phase_settings[5]))
                            go = True
                            signal = 0
                            n_amps = {x: 0 for x in range(5)}
                            iterations = {x: 0 for x in range(5)}
                            real_input_data = {x: input_data for x in range(5)}
                            iteration = 0
                            while go:
                                # print(n_amps)
                                print('trying 1', signal, phase_settings)
                                (amp_1, opcode) = process(0, signal, i1)
                                print('trying 2', opcode)
                                (amp_2, opcode) = process(1, amp_1, i2)
                                print('trying 3', opcode)
                                (amp_3, opcode) = process(2, amp_2, i3)
                                print('trying 4', opcode)
                                (amp_4, opcode) = process(3, amp_3, i4)
                                print('trying 5', opcode)
                                (amp_5, opcode) = process(4, amp_4, i5)
                                signal = amp_5
                                if opcode == 99:
                                    print('Ending program', signal)
                                    go = False
                                    if signal > result:
                                        result = amp_5
                                        best_phase_setting = str(phase_settings[1])+str(phase_settings[2])+str(phase_settings[3])+str(phase_settings[4])+str(phase_settings[5])
                                        print('setting result to', signal, best_phase_setting)
                                    else:
                                        print(signal, result)
                                # elif opcode == 4:
                                #     print('restart')
                                # else:
                                #     print('restart')
                                iteration += 1

                        except Exception as e:
                            raise e
                            continue
    print('count', count)
    print('best_phase_setting', best_phase_setting)



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


# 5693519 too high