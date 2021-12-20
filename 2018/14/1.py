# IMPORTS
from os import path
import math
import numpy as np
import pprint
import re

# SETUP
input_file = path.splitext(path.basename(__file__))[0] + '.txt'
if not path.isfile(input_file):
    input_file = '1.txt'

with open(input_file) as f:
    input_data = f.read()

if not input_data:
    raise Exception('No content !')

result = None


# FUNCTIONS


def ppprint(message, file=None):
    np.set_printoptions(threshold=np.nan)
    pp = pprint.PrettyPrinter(indent=4, stream=file)
    pp.pprint(message)


# SOLUTION GOES HERE


def main():
    global input_data, result

    max_recipes = int(input_data) + 10

    recipes = [3, 7]
    current_recipes = [0, 1]

    result = max_recipes

    while len(recipes) < max_recipes:
        # print(current_recipes)
        # print(recipes)
        new_recipes = [int(i) for i in list(
            str(sum([recipes[i] for i in current_recipes])))]
        recipes.extend(new_recipes)
        current_recipes = [(current + recipes[current] + 1) %
                           len(recipes) for current in current_recipes]

    result = int(''.join([str(i) for i in recipes[-10:]]))


if __name__ == "__main__":
    main()


# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
