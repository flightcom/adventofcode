# IMPORTS
from os import path
from functools import reduce
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
    if item not in steps_prev:
        if item in steps_next and item not in processed and item in available_steps:
            return True
        else:
            return False
    else:
        for key in steps_prev[item]:
            if not key in processed:
                return False
    return True


def process(current: str):
    global available_steps, workers, workers_limit, time_padding
    being_processed = [worker[0] for worker in workers]
    if len(workers) < workers_limit and current not in being_processed:
        workers.append((current, ord(current) - 64 + time_padding))
        available_steps.remove(current)


def get_first_available_step():
    available_steps.sort()
    return available_steps[0] if len(available_steps) else None


def check_available_steps():
    global available_steps, first_steps, processed, being_processed, workers, steps_next, steps_prev, workers, last_step
    being_processed = [worker[0] for worker in workers]
    # Test
    test, test2, test3 = False, False, False
    available_steps = []
    for step in steps_next:
        # check if in first steps
        test = step in first_steps and step not in being_processed and step not in processed
        # check if not first step
        if step in steps_prev:
            test2 = step not in being_processed and step not in processed
            test3 = [step2 in processed for step2 in steps_prev[step]]
            test3 = reduce((lambda a, b: a and b), test3) if test3 else False
        available = test or (test2 and test3)
        if available:
            available_steps.append(step)

    # check last step
    last_step_ready = reduce((lambda a, b: a and b), [
                             step in processed for step in steps_prev[last_step]]) and last_step not in being_processed
    if last_step_ready:
        available_steps.append(last_step)


def run():
    global available_steps, workers, total_time, processed
    total_time += 1
    workers = [(x[0], x[1] - 1) for x in workers if x[1] > 0]
    for worker in workers:
        if worker[1] == 0:
            processed.append(worker[0])
    workers = [worker for worker in workers if worker[1] != 0]


def is_free_workers():
    global workers_limit, workers
    return workers_limit - len(workers) > 0


def main():
    global result, steps_next, steps_prev, processed, first_steps, available_steps, workers, workers_limit, time_padding, total_time, last_step

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

    first_steps = list(steps_next_keys - steps_prev_keys)
    last_step = list(steps_prev_keys - steps_next_keys)[0]

    available_steps = list(sorted(first_steps))
    processed = []

    # Params
    workers = []
    workers_limit = 5
    time_padding = 60
    total_time = 0

    current = None

    while last_step not in processed:
        check_available_steps()
        while is_free_workers() and get_first_available_step():
            current = get_first_available_step()
            process(current)
            check_available_steps()
        run()

    result = ''.join(processed)
    result = total_time


if __name__ == "__main__":
    main()

# OUTPUT RESULT
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(result)
