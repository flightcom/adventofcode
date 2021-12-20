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
input_file = path.splitext(path.basename(__file__))[0].split('.')[0] + '.txt'
# input_file = path.splitext(path.basename(__file__))[0] + '.test.txt'

with open(input_file) as f:
    input_data = f.read()
# with open(input_file) as f:
#     input_data = f.read().split()

if not input_data:
    raise Exception('No content !')

# GLOBAL VARIABLES
result = None

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
def main():
    global input_data, result
    image_dimensions = { "height": 6, "width": 25}
    pixels_per_layer = image_dimensions['height']*image_dimensions['width']
    number_of_layers = int(len(input_data)/(image_dimensions['height']*image_dimensions['width']))

    print(pixels_per_layer, number_of_layers)

    layers = [input_data[n*pixels_per_layer:(n+1)*pixels_per_layer] for n in range(number_of_layers)]

    first_column = [int(n[0]) for n in layers]
    columns = [[int(n[i]) for n in layers] for i in range(len(layers[0]))]

    final_layer = [list(filter(lambda a: a != 2, columns[i]))[0] for i in range(len(layers[0]))]
    final_layer = ['#' if x != 1 else ' ' for x in final_layer]
    final_layer = [''.join(final_layer[i:i+image_dimensions['width']]) for i in range(0, len(final_layer), image_dimensions['width'])]

    result = final_layer


if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)
