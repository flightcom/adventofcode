from os import path
import numpy as np

# SETUP
input_file = path.basename(__file__) + '.txt'
if not path.isfile(input_file): 
    input_file = '01.txt'

with open(input_file) as f:
    input_data = f.read().splitlines() 


if not input_data:
    raise Exception('No content !')

# SOLUTION GOES HERE

x_max = max([int(entry.split(',')[0]) for entry in input_data])
x_min = min([int(entry.split(',')[0]) for entry in input_data])

y_max = max([int(entry.split(',')[1]) for entry in input_data])
y_min = min([int(entry.split(',')[1]) for entry in input_data])

x_padding = x_min
y_padding = y_min

matrix = np.empty([x_max - x_padding, y_max - y_padding])
matrix.fill(-1)

processed_data = [[int(split) for split in entry.split(',')] for entry in input_data]
processed_data = [[entry[0] - x_padding, entry[1] - y_padding] for entry in processed_data]

# For each position in the map, compute Manhattan distance from every point
# If minimum value corresponds to only one point, the position takes the index of that point
# Else, stays as null

def total_distance(p: list):
    distances = [manhattan_distance(p, point) for point in processed_data]
    return sum(distances)

def manhattan_distance(p1: list, p2: list):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2-x1) + abs(y2-y1)


for (x,y), value in np.ndenumerate(matrix):
    matrix[x,y] = total_distance([x,y])

matrix_flatten = list(matrix.flatten().astype(int))

area_surface = sum(i < 10000 for i in matrix_flatten)

result = area_surface

# OUTPUT RESULT
print(result)
