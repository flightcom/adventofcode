# IMPORTS
from os import path
import numpy as np
import pprint
import re

# SETUP
input_file = path.splitext(path.basename(__file__))[0] + '.txt'
input_file = '1.txt'
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


# def process(node: list):

def process2(liste: list):
    global total, values

    while liste[0] != None:
        # print('---')
        # print(len([l for l in liste if l != None]))
        for index, n in enumerate(liste):
            # print(index)
            # if we reach a node with no subnode
            if n == 0:
                # check if former parent
                # node = liste[index:index+2+liste[index+1]]
                # print(node)
                # node_no_header = node[2:]
                # node_items = list(set(node_no_header))
                if liste[index+2] == None:
                    # Compare metadaentries values and # of children
                    parent_end = min([i for i, m in enumerate(
                        liste) if m != None and i > index + 1]) + liste[index+1]
                    parent_start = index
                    parent = liste[parent_start:parent_end]
                    # print(parent)
                    metadataentries = parent[-parent[1]:]

                    # Count children listed in values
                    values_filtered = [
                        y for x, y in values.items() if x >= index+2 and x < index+len(parent)]
                    values_x_filtered = [
                        x for x, y in values.items() if x >= index+2 and x < index+len(parent)]
                    # print(parent)
                    # print(metadataentries)
                    # print(values_filtered)
                    children_values = [values_filtered[i-1]
                                       for i in metadataentries if len(values_filtered) >= i]

                    values[index] = sum(children_values)
                    # remove previous values
                    # print(metadataentries)
                    # print(index+2, index+len(parent))
                    # print(values_filtered)
                    # print(children_values)
                    # print(index, index+len(parent))
                    values = {
                        x: y for x, y in values.items() if x not in values_x_filtered}

                    liste = [l if i not in range(
                        index, index+len(parent)) else None for i, l in enumerate(liste)]
                    # total += sum(children_values)
                else:
                    # Check if not first child
                    node = liste[index:index+2+liste[index+1]]

                    # store value
                    metadataentries = node[2:2+node[1]]
                    sum_metadataentries = sum(metadataentries)
                    values[index] = sum_metadataentries

                    liste = [l if i not in range(
                        index, index+len(node)) else None for i, l in enumerate(liste)]
                # decrement parent # of children
                if liste[index-2] != None:
                    parent_start = index-2
                else:
                    # print('before')
                    subliste = [i for i, m in enumerate(
                        liste) if m != None and i < index - 1]

                    if len(subliste) > 0:
                        parent_start = max([i for i, m in enumerate(
                            liste) if m != None and i < index - 1]) - 1
                    # else:
                    #     parent_start = 0

                # print(parent_start, liste[parent_start])

                if liste[parent_start]:
                    liste[parent_start] -= 1
                # print(liste)
                # print(values)
                break
        # print(len(liste))


def main():
    global result, total, values

    liste = list(map(int, input_data))
    total = 0
    values = {}

    process2(liste)
    print(values)
    print(values[0])
    quit()

    # result = total


    # RUN
if __name__ == "__main__":
    main()

# OUTPUT RESULT
pp = pprint.PrettyPrinter(indent=4)
if result:
    pp.pprint(result)
