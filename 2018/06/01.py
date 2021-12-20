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

def closest_point(p: list):
    distances = [(index, manhattan_distance(p, point)) for index, point in enumerate(processed_data)]
    sorted_distances = sorted(distances, key=lambda x: x[1]) 
    return sorted_distances[0][0]

def manhattan_distance(p1: list, p2: list):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2-x1) + abs(y2-y1)


for (x,y), value in np.ndenumerate(matrix):
    matrix[x,y] = closest_point([x,y])

matrix_flatten = matrix.flatten().astype(int)
counts = np.bincount(matrix_flatten)
max_occuring = list(matrix_flatten).count(np.argmax(counts))

result = max_occuring

# OUTPUT RESULT
print(result)
