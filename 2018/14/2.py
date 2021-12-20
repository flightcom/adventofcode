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

with open(input_file) as f:
    input_data = f.read()
# with open(input_file) as f:
#     input_data = f.read().split()
# with open(input_file) as f:
#     input_data = f.read().splitlines()


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


def main():
    global input_data, result

    my_score = input_data

    recipes = '37'
    current_recipes = [0, 1]

    while my_score not in recipes[-len(my_score):]:
        new_recipes = str(sum([int(recipes[i]) for i in current_recipes]))
        recipes += new_recipes
        current_recipes = [(current + int(recipes[current]) + 1) %
                           len(recipes) for current in current_recipes]

    # result = len(recipes) - len(my_score)
    result = recipes.index(my_score)


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


# 290431
# 20696327
