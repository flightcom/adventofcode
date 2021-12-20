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

# with open(input_file) as f:
#     input_data = f.read()
# with open(input_file) as f:
#     input_data = f.read().split()
with open(input_file) as f:
    input_data = f.read().splitlines()
# input_data = np.loadtxt(input_file, dtype=np.object)

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
    # ppprint(input_data)
    moons = [{
        'x': int(re.match("^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$", entry).groups()[0]), 
        'y': int(re.match("^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$", entry).groups()[1]), 
        'z': int(re.match("^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$", entry).groups()[2]),
        'vx': 0, 
        'vy': 0, 
        'vz': 0
        } for entry in input_data]
    ppprint(moons)

    initialState = moons
    go = True

    maxx = {
        "x": 0,
        "y": 0,
        "z": 0,
    }

    minn = {
        "x": 0,
        "y": 0,
        "z": 0,
    }

    n = 0
    while go:
        changes = [
            ((sum([n['x'] < moon['x'] for j, n in enumerate(moons) if j != index]), sum([n['x'] > moon['x'] for j, n in enumerate(moons) if j != index])),
            (sum([n['y'] < moon['y'] for j, n in enumerate(moons) if j != index]), sum([n['y'] > moon['y'] for j, n in enumerate(moons) if j != index])),
            (sum([n['z'] < moon['z'] for j, n in enumerate(moons) if j != index]), sum([n['z'] > moon['z'] for j, n in enumerate(moons) if j != index])))
            for index, moon in enumerate(moons)
        ]
        energy = sum([(abs(moon['x']) + abs(moon['y']) + abs(moon['z'])) * 
                (abs(moon['vx']) + abs(moon['vy']) + abs(moon['vz'])) for moon in moons])

        moons = [
            {
                'vx': moon['vx'] - changes[i][0][0] + changes[i][0][1],
                'vy': moon['vy'] - changes[i][1][0] + changes[i][1][1],
                'vz': moon['vz'] - changes[i][2][0] + changes[i][2][1],
                'x': moon['x'] + moon['vx'] - changes[i][0][0] + changes[i][0][1],
                'y': moon['y'] + moon['vy'] - changes[i][1][0] + changes[i][1][1],
                'z': moon['z'] + moon['vz'] - changes[i][2][0] + changes[i][2][1],
            } for i, moon in enumerate(moons)
        ]
        if moons == initialState:
            go = False
        # else:
        #     states.append(moons)

        # if n % 10000 == 0:
        #     print(n)
        n += 1

        maxx['x'] = max(maxx['x'], max([moon['x'] for moon in moons]))
        maxx['y'] = max(maxx['y'], max([moon['y'] for moon in moons]))
        maxx['z'] = max(maxx['z'], max([moon['z'] for moon in moons]))

        minn['x'] = min(minn['x'], min([moon['x'] for moon in moons]))
        minn['y'] = min(minn['y'], min([moon['y'] for moon in moons]))
        minn['z'] = min(minn['z'], min([moon['z'] for moon in moons]))

        pot_energy = sum([(abs(moon['x']) + abs(moon['y']) + abs(moon['z'])) for moon in moons])
        kin_energy = sum([(abs(moon['vx']) + abs(moon['vy']) + abs(moon['vz'])) for moon in moons])

        print(n, maxx, minn, energy, pot_energy, kin_energy)
        # print(n, energy)
        # exit()
    result = n


if __name__ == "__main__":
    main()

# OUTPUT RESULT
try:
    result
except NameError:
    print("Result is not defined")
else:
    ppprint(result)


# 1870813536