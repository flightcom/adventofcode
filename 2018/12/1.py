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


def main():
    global input_data, result

    match = re.match(
        "^initial state: ([.#]+)$", input_data[0])

    initial_state = match.groups()[0]
    stride = 5
    n_cycles = 20

    rules = {x: y for x, y in [item.split(' => ') for item in input_data[2:]]}

    initial_state = list(initial_state)
    length_before = len(initial_state)
    initial_state = pad_state(initial_state, n_cycles, stride)
    current_state = initial_state
    length_after = len(initial_state)

    print(''.join(current_state))
    for i in range(n_cycles):
        intermediary_state = current_state[:]
        for j in range(length_after - stride + 1):
            start = j
            end = j + stride
            part = current_state[start:end]
            part_joined = ''.join(part)
            if part_joined in rules:
                new_char = rules[part_joined]
            else:
                new_char = '.'
            intermediary_state[j+2] = new_char
        current_state = intermediary_state[:]
        print(''.join(current_state))

    total = 0
    # count
    for index, pot in enumerate(current_state):
        key = index - (length_after - length_before)/2
        if pot == '#':
            total += key

    result = total


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
