# IMPORTS
from os import path
from scipy import stats
from functools import reduce
import math
import numpy as np
import pprint
import re
import copy
# import matplotlib.pyplot as plt
from numpy import unravel_index
import sys, getopt
import operator

# SETUP
# input_file = path.splitext(path.basename(__file__))[0] + '.test.txt'
input_file = path.splitext(path.basename(__file__))[0] + '.txt'
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

result = 0

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

def main(argv):
    opts, args = getopt.getopt(argv,'')
    if args[0] == '1':
        return part1()
    if args[0] == '2':
        return part2()


# SOLUTION GOES HERE

def part1():
    global input_data
    i = 0
    authorized = []
    while input_data[i] != "":
        part = input_data[i].split(': ')[1]
        part_n1 = part.split(' or ')[0]
        part_n2 = part.split(' or ')[1]
        for n1 in range(int(part_n1.split('-')[0]), int(part_n1.split('-')[1])+1):
            authorized.append(n1)
        for n2 in range(int(part_n2.split('-')[0]), int(part_n2.split('-')[1])+1):
            authorized.append(n2)
        i += 1

    authorized = list(set(authorized))

    i += 2
    my_ticket = [int(m) for m in input_data[i].split(',')]

    i += 3
    error_rate = 0
    while i < len(input_data):
        ticket = [int(m) for m in input_data[i].split(',')]
        error_rate += ticket_error_rate(authorized, ticket)
        i += 1

    return error_rate


def part2():
    global input_data
    i = 0
    authorized = {}
    while input_data[i] != "":
        [name, part] = input_data[i].split(': ')
        authorized[name] = []
        part_n1 = part.split(' or ')[0]
        part_n2 = part.split(' or ')[1]
        for n1 in range(int(part_n1.split('-')[0]), int(part_n1.split('-')[1])+1):
            authorized[name].append(n1)
        for n2 in range(int(part_n2.split('-')[0]), int(part_n2.split('-')[1])+1):
            authorized[name].append(n2)
        i += 1

    # authorized = list(set(authorized))

    i += 2
    my_ticket = [int(m) for m in input_data[i].split(',')]

    i += 3
    error_rate = 0
    t = 0
    tickets = []
    while i < len(input_data):
        ticket = [int(m) for m in input_data[i].split(',')]
        error_rate = ticket_error_rate2(authorized, ticket)
        if error_rate == 0:
            tickets.append(ticket)
        i += 1
        t += 1


    print(t, len(tickets))

    # on prend la premiere valeur de chaque ticket
    # on passe ces valeurs avec authorized a une fonction
    values_flatten = [[t[i] for t in tickets] for i in range(len(tickets[0]))]
    # print(values_flatten)
    keys = []

    for vs in values_flatten:
        key = get_valid_keys(vs, authorized)
        print(key)
        # authorized.pop(key, None)
        keys.append(key)

    # print(keys, [len(k) for k in keys])
    # exit()

    # At this point, we identified the possible keys for each number
    # We need to iterate through the keys array and remove the possibilities in
    # other lines
    length = 0
    while length < len(keys):
        length = 0
        for i, k in enumerate(keys):
            print(k, len(k))
            if len(k) == 1:
                print('only one for {}'.format(k[0]))
                length += 1
                v = k[0]
                [k1.remove(v) for i1, k1 in enumerate(keys) if v in k1 and i1 != i]

    values = []

    keys = [k[0] for k in keys]

    for i, k in enumerate(keys):
        if k != None and k.startswith("departure"):
            values.append(my_ticket[i])

    print(values)
    return np.prod(values)

def ticket_is_valid(authorized, ticket):
    v = [t in authorized for t in ticket]
    return all(p == True for p in v)


def ticket_error_rate(authorized, ticket):
    not_allowed = []
    for v in ticket:
        if v not in authorized:
            not_allowed.append(v)
    return sum(not_allowed)

def ticket_error_rate2(authorized, ticket):
    not_allowed = []
    for v in ticket:
        found = False
        for k in authorized.keys():
            if v in authorized[k]:
                found = True
                continue
        if not found:
            not_allowed.append(v)
    return sum(not_allowed)

def get_valid_key(values, authorized):
    key = None
    for k in reversed(authorized.keys()):
    # for k in authorized.keys():
        check = all(item in authorized[k] for item in values)
        if check is True:
            # print('yes', k, authorized[k], values)
            key = k
            break
        # else:
        #     print('no', k, authorized[k], values)
    # print(key)
    return key

def get_valid_keys(values, authorized):
    keys = []
    for k in reversed(authorized.keys()):
    # for k in authorized.keys():
        check = all(item in authorized[k] for item in values)
        if check is True:
            # print('yes', k, authorized[k], values)
            keys.append(k)
        # else:
        #     print('no', k, authorized[k], values)
    # print(key)
    return keys



if __name__ == "__main__":
    result = main(sys.argv[1:])


# OUTPUT RESULT
try:
    print(result)
except NameError:
    print("Result is not defined")


# 8911854359477 too high
# 589685618167