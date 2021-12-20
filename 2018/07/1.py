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
    input_data = f.read().splitlines()


if not input_data:
    raise Exception('No content !')


# SOLUTION GOES HERE

def can_process(item):
    if not item in steps_prev:
        return True
    for key in steps_prev[item]:
        if not key in processed:
            return False
    print('Processing {}'.format(item))
    return True


def get_first_available_step():
    available_steps.sort()
    return available_steps[0] if len(available_steps) else None


def main():
    global result, steps_next, steps_prev, processed, available_steps

    steps_next = {}
    steps_prev = {}

    for entry in input_data:
        match = re.match(
            "^Step (\w) must be finished before step (\w) can begin\.$", entry)
        step_from = match.groups()[0]
        step_to = match.groups()[1]
        if step_from in steps_next:
            steps_next[step_from].append(step_to)
        else:
            steps_next[step_from] = [step_to]

        if step_to in steps_prev:
            steps_prev[step_to].append(step_from)
        else:
            steps_prev[step_to] = [step_from]

    steps_next_keys = steps_next.keys()
    steps_prev_keys = steps_prev.keys()

    difference = steps_next_keys - steps_prev_keys

    available_steps = list(sorted(difference))
    processed = []
    current = get_first_available_step()

    while current:
        if can_process(current):
            processed.append(current)
            available_steps.remove(current)
            if current in steps_next:
                available_steps.extend(steps_next[current])
            nodupes = []
            [nodupes.append(x)
             for x in available_steps if not nodupes.count(x)]
            available_steps = nodupes
        else:
            available_steps.remove(current)

        current = get_first_available_step()

    result = ''.join(processed)


if __name__ == "__main__":
    main()

# OUTPUT RESULT
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(result)
