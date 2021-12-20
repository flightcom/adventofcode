# IMPORTS
from os import path
from scipy import stats
import math
import numpy as np
import pprint
import re
# import matplotlib.pyplot as plt
from numpy import unravel_index
import turtle

# SETUP
input_file = path.splitext(path.basename(__file__))[0].split('.')[0] + '.txt'
input_file = path.splitext(path.basename(__file__))[0] + '.test.txt'
# input_file = 'test.txt'
if not path.isfile(input_file):
    input_file = '1.txt'

# with open(input_file) as f:
#     input_data = f.read()
# with open(input_file) as f:
#     input_data = f.read().split()
with open(input_file) as f:
    input_data = f.read().splitlines()


if not input_data:
    raise Exception('No content !')

# GLOBAL VARIABLES
result = 0
split_data = None
real_input_data = None
relative_base = 0
n = 0

# FUNCTIONS
def ppprint(message, file=None):
    # np.set_printoptions(threshold=np.nan)
    pp = pprint.PrettyPrinter(indent=4, stream=file, width=150)
    pp.pprint(message)


def draw(X, Y):
    plt.plot(X, Y, 'ro')
    # Reverse Y-Axis
    plt.gca().invert_yaxis()
    plt.show()

# SOLUTION GOES HERE
def get_reaction_that_produces(reactions: list, element: str):
    for index, reaction in enumerate(reactions):
        if reaction[1][1] == element:
            return index
    return False

def main():
    global input_data, result
    # print(input_data)
    reactions = []
    need_to_produce = {'FUEL': 1}
    reg = '^((\d+ \w+)((, \d+ \w+)+)?) => (\d+ \w+)$'
    for inp in input_data:
        # print(inp)
        match = re.match(reg, inp)
        reactions.append(([entry.split(' ') for entry in match.groups()[0].split(', ')], match.groups()[-1].split(' ')))

    ppprint(reactions)
    # print('ORE' not in need_to_produce.keys())

    n = 0
    elementary = False

    index = get_reaction_that_produces(reactions, 'FUEL')
    my_reaction = reactions[index]
    my_reaction = my_reaction[0]
    primary_elements = [item[1][1] for item in reactions if len(item[0]) == 1 and item[0][0][1] == 'ORE']

    leftovers = {}

    while not elementary:
        my_next_reaction = my_reaction
        elementary = sum([p not in primary_elements for q,p in my_reaction]) == 0
        # for q, p in my_reaction:
        #     if p not in primary_elements:
        #         elementary = False
        for i, (q, p) in enumerate(my_reaction):
            # print(q, p)
            q = int(q)
            if p in primary_elements:
                continue
            else:
                index = get_reaction_that_produces(reactions, p)
                q_o = int(reactions[index][1][0])
                if p in leftovers:
                    q1 = q
                    q -= leftovers[p]
                    leftovers.pop(p, None)
                    quotient = math.ceil(q / q_o)
                    # print(q_o, q, quotient, 'leftover', q1)
                else:
                    quotient = math.ceil(q / q_o)
                    # print(q_o, q, quotient, q_o * quotient - int(q))
                if q_o * quotient - int(q) > 0:
                    if p in leftovers:
                        leftovers[p] += q_o * quotient - int(q)
                    else:
                        leftovers[p] = q_o * quotient - int(q)
                    print('adding', q_o * quotient - int(q), p, 'to leftovers')
                for inp in reactions[index][0]:
                    prod = inp[1]
                    quan = int(inp[0]) * quotient
                    found = False
                    for item in my_next_reaction:
                        if item[1] == prod:
                            item[0] = int(item[0]) + quan
                            found = True
                    if not found:
                        my_next_reaction.append([quan, prod])
                my_next_reaction.pop(i)
        my_reaction = my_next_reaction
        print(my_reaction)

    print('ELEMENTARY')
    final_elements = {}
    for element in my_reaction:
        (q,p) = element
        if p in final_elements:
            final_elements[p] += int(q)
        else:
            final_elements[p] = int(q)
    print(final_elements)

    result = 0

    for key, value in final_elements.items():
        # print(key, value)
        index = get_reaction_that_produces(reactions, key)
        q_o = int(reactions[index][1][0])
        quotient = math.ceil(value / q_o)
        print(key, q_o, quotient, reactions[index][0][0])
        result += quotient * int(reactions[index][0][0][0])

    ppprint(leftovers)

if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)


# 796848 too high