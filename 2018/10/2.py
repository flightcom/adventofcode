# IMPORTS
from os import path
from scipy import stats
import numpy as np
import pprint
import re
import matplotlib.pyplot as plt

# SETUP
input_file = path.splitext(path.basename(__file__))[0] + '.txt'
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


def ppprint(message):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(message)


def draw(X, Y):
    plt.plot(X, Y, 'ro')
    # Reverse Y-Axis
    plt.gca().invert_yaxis()
    plt.show()

# SOLUTION GOES HERE


def main():
    global input_data, result

    points = {}
    found = False
    previous_max_occurence = 0

    # Process input
    for index, entry in enumerate(input_data):
        match = re.match(
            "^position=<\s?([-]?\d+), \s?([-]?\d+)> velocity=<\s?([-]?\d+), \s?([-]?\d+)>$", entry)

        x = int(match.groups()[0])
        y = int(match.groups()[1])
        x_speed = int(match.groups()[2])
        y_speed = int(match.groups()[3])

        point = {
            'x': x,
            'y': y,
            'x_speed': x_speed,
            'y_speed': y_speed,
        }

        points[index] = point

    n_points = len(points)

    # Test draw
    # X = [point['x'] for index, point in points.items()]
    # Y = [point['y'] for index, point in points.items()]
    # draw(X, Y)
    # quit()

    # Check y for message (the more points there are with same y, the most probable the message is to be)
    # We can start with 5% of the points with same y
    iteration = 0

    while not found:
        iteration += 1
        # Move points
        for i, point in points.items():
            point['x'] += point['x_speed']
            point['y'] += point['y_speed']

        Y = [point['y'] for index, point in points.items()]

        stat = stats.mode(Y)
        item = stat.mode[0]
        item_n_occurences = stat.count[0]

        # if previous_max_occurence > item_n_occurences:
        if item_n_occurences > n_points * 0.1:
            X = [point['x'] for index, point in points.items()]
            Y = [point['y'] for index, point in points.items()]

            stat = stats.mode(Y)
            item = stat.mode[0]
            item_n_occurences = stat.count[0]

            print(iteration)
            found = True

        previous_max_occurence = item_n_occurences


if __name__ == "__main__":
    main()

# OUTPUT RESULT
if result:
    ppprint(result)
