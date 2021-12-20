# IMPORTS
from os import path
import numpy as np
import pprint
import re

# SETUP
input_file = path.splitext(path.basename(__file__))[0] + '.txt'
if not path.isfile(input_file):
    input_file = '1.txt'

with open(input_file) as f:
    input_data = f.read().split()


if not input_data:
    raise Exception('No content !')


result = None

# SOLUTION GOES HERE


def get_header(node: list):
    return node[:2]


def get_number_of_metadataentries(node: list):
    return int(node[1:2][0])


def get_number_of_subnodes(node: list):
    return int(node[:1][0])


def main():
    global result

    liste = list(map(int, input_data))
    total = 0

    while len(liste) > 0:
        for index, n in enumerate(liste):
            # if we reach a node with no subnode
            if n == 0:
                node = liste[index:index+2+liste[index+1]]
                metadataentries = node[2:2+node[1]]
                # Sum metadataentries
                total += sum(metadataentries)
                # Decrement parent node counter
                liste[index-2] -= 1
                # Remove node from list
                liste = [l for i, l in enumerate(
                    liste) if i not in range(index, index+2+liste[index+1])]
                break
    result = total


    # RUN
if __name__ == "__main__":
    main()

# OUTPUT RESULT
pp = pprint.PrettyPrinter(indent=4)
if result:
    pp.pprint(result)
