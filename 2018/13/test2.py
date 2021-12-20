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


def get_positions(carts):
    return [cart['position'] for cart in carts]


def move_cart(cart, carte):
    drctn = cart['direction']
    position = cart['position']
    # Direction is relative to map
    # Turn is relative to cart
    if drctn == 'L':  # X decreasing
        position = (position[0]-1, position[1])
        if carte[position[1]][position[0]] == '+':
            if cart['turn'] == 'L':
                cart['direction'] = 'D'
                cart['turn'] = 'S'
            elif cart['turn'] == 'R':
                cart['direction'] = 'U'
                cart['turn'] = 'L'
            elif cart['turn'] == 'S':
                cart['turn'] = 'R'
        elif carte[position[1]][position[0]] == '/':
            cart['direction'] = 'D'
        elif carte[position[1]][position[0]] == '\\':
            cart['direction'] = 'U'
    elif drctn == 'U':  # Y decreasing
        position = (position[0], position[1]-1)
        if carte[position[1]][position[0]] == '+':
            if cart['turn'] == 'L':
                cart['direction'] = 'L'
                cart['turn'] = 'S'
            elif cart['turn'] == 'R':
                cart['direction'] = 'R'
                cart['turn'] = 'L'
            elif cart['turn'] == 'S':
                cart['turn'] = 'R'
        elif carte[position[1]][position[0]] == '/':
            cart['direction'] = 'R'
        elif carte[position[1]][position[0]] == '\\':
            cart['direction'] = 'L'
    elif drctn == 'R':  # X increasing
        position = (position[0]+1, position[1])
        if carte[position[1]][position[0]] == '+':
            if cart['turn'] == 'L':
                cart['direction'] = 'U'
                cart['turn'] = 'S'
            elif cart['turn'] == 'R':
                cart['direction'] = 'D'
                cart['turn'] = 'L'
            elif cart['turn'] == 'S':
                cart['turn'] = 'R'
        elif carte[position[1]][position[0]] == '/':
            cart['direction'] = 'U'
        elif carte[position[1]][position[0]] == '\\':
            cart['direction'] = 'D'
    elif drctn == 'D':  # X increasing
        position = (position[0], position[1]+1)
        if carte[position[1]][position[0]] == '+':
            if cart['turn'] == 'L':
                cart['direction'] = 'R'
                cart['turn'] = 'S'
            elif cart['turn'] == 'R':
                cart['direction'] = 'L'
                cart['turn'] = 'L'
            elif cart['turn'] == 'S':
                cart['turn'] = 'R'
        elif carte[position[1]][position[0]] == '/':
            cart['direction'] = 'L'
        elif carte[position[1]][position[0]] == '\\':
            cart['direction'] = 'R'
    cart['position'] = position
    return position


def move_carts(carts, carte):
    global result

    iteration = 0
    crash = False

    while not crash:
        iteration += 1
        print('Iteration {}'.format(iteration))
        print(len(carts))
        if len(carts) == 1:
            result = carts[0]
            return
        ppprint(carts)
        # Move carts
        moved_carts = []
        carts_to_remove = []
        for y, _row in enumerate(carte):
            for x, _col in enumerate(carte[y]):
                # print(x, y)
                positions = get_positions(carts)
                if (x, y) in positions:
                    index = positions.index((x, y))
                    if index not in moved_carts:
                        position = move_cart(carts[index], carte)
                        moved_carts.append(index)
                    # Check positions: if two carts have the same positions ==> Crash !
                    carts_filtered = [cart for i, cart in enumerate(
                        carts) if i not in carts_to_remove]
                    positions = get_positions(carts_filtered)
                    if len(positions) != len(set(positions)):
                        crashed_carts_indexes = [i for i, cart in enumerate(
                            carts) if cart['position'] == position]
                        carts_to_remove.extend(crashed_carts_indexes)
        carts_to_remove.sort()
        print(carts_to_remove)
        for index in carts_to_remove[::-1]:
            carts.pop(index)


def analyze_map(carte):
    carts = []
    for y, row in enumerate(carte):
        for x, col in enumerate(row):
            if carte[y][x] in ['v', '^', '<', '>']:
                cart = {
                    'position': (x, y),
                    # Down, Up, Left, Right
                    'direction': 'D' if carte[y][x] == 'v' else 'U' if carte[y][x] == '^' else 'L' if carte[y][x] == '<' else 'R',
                    'turn': 'L'
                }
                carts.append(cart)
    return carts

# Cart:
## - position
## - direction
# - last intersection direction (left, straight, right)


def main():
    global input_data, result

    carte = input_data
    carts = analyze_map(input_data)

    move_carts(carts, carte)
    # ppprint(len(carts))

    # print(input_data[0][42])


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
