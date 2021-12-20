# IMPORTS
from os import path
from scipy import stats
import math
import numpy as np
import pprint
import re
import matplotlib.pyplot as plt
from numpy import unravel_index

# SETUP
input_file = path.splitext(path.basename(__file__))[0] + '.txt'
# input_file = 'test.txt'
if not path.isfile(input_file):
    input_file = '1.txt'

# with open(input_file) as f:
#     input_data = f.read().split()
with open(input_file) as f:
    input_data = f.read().splitlines()


if not input_data:
    raise Exception('No content !')


result = None

# FUNCTIONS


def ppprint(message, file=None):
    np.set_printoptions(threshold=np.nan)
    pp = pprint.PrettyPrinter(indent=4, stream=file)
    pp.pprint(message)


def draw(X, Y):
    plt.plot(X, Y, 'ro')
    # Reverse Y-Axis
    plt.gca().invert_yaxis()
    plt.show()

# SOLUTION GOES HERE


def pad_state(state, n_cycles, stride):
    pad = ['.'] * (n_cycles + math.floor(stride/2))
    state = pad + state + pad
    return state


def get_sum(state, length_before):
    total = 0
    length_after = len(state)

    # count
    for index, pot in enumerate(state):
        key = index - (length_after - length_before)/2
        if pot == '#':
            total += key

    return total


def main():
    global input_data, result

    match = re.match(
        "^initial state: ([.#]+)$", input_data[0])

    initial_state = match.groups()[0]
    stride = 5
    n_cycles = 500
    # n_cycles = 50000000000

    rules = {x: y for x, y in [item.split(' => ') for item in input_data[2:]]}

    initial_state = list(initial_state)
    length_before = len(initial_state)
    current_state = initial_state
    somme = 0

    for i in range(n_cycles):
        if i % 1000 == 0 and i != 0:
            print(i)
        current_state = pad_state(current_state, 1, stride)
        intermediary_state = current_state[:]
        # print(''.join(intermediary_state))
        length = len(intermediary_state)
        for j in range(length - stride + 1):
            start = j
            end = j + stride
            part = current_state[start:end]
            part_joined = ''.join(part)
            # print(part_joined)
            new_char = rules[part_joined]
            intermediary_state[j+2] = new_char
        current_state = intermediary_state[:]
        # print(''.join(current_state))
        previous_somme = somme
        somme = get_sum(current_state, length_before)
        print(somme - previous_somme)

    result = somme


if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
    # with open('out.txt', 'w') as f:
    #     ppprint(result, file=f)  # Python 3.x
