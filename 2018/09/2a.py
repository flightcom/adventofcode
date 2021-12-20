# IMPORTS
from os import path
import numpy as np
import pprint
import re

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

# SOLUTION GOES HERE


def main():
    global input_data, result

    input_data = input_data[0]

    match = re.match(
        "^(\d+) players; last marble is worth (\d+) points$", input_data)

    n_players = int(match.groups()[0])
    last_marble = int(match.groups()[1]) * 100
    scores = {}

    current_marble_position = 0
    current_player = 0
    iteration = 1  # also used for next marble

    marbles = [0]

    while iteration <= last_marble:
        if iteration % 10000 == 0:
            print(iteration)
        if iteration % 23 != 0:
            current_marble_position = (
                current_marble_position + 1) % len(marbles) + 1
            marbles.insert(current_marble_position, iteration)
        else:
            # add marble to current player score
            if current_player not in scores:
                scores[current_player] = iteration
            else:
                scores[current_player] += iteration
            current_marble_position = (
                current_marble_position - 7) % len(marbles)
            scores[current_player] += marbles[current_marble_position]
            marbles.pop(current_marble_position)
        iteration += 1
        current_player = (current_player+1) % n_players
        # print(marbles)

    winning_player = max(scores, key=scores.get)
    print(scores[winning_player])


if __name__ == "__main__":
    main()

# OUTPUT RESULT
pp = pprint.PrettyPrinter(indent=4)
if result:
    pp.pprint(result)


# Part two result is : 3212081616
