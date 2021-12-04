import numpy as np
from copy import deepcopy

def read_input(filename='inputs/day04.txt'):
    with open(filename) as f:
        inp = f.read().split('\n\n')
    numbers = list(map(int, inp.pop(0).strip().split(',')))
    boards = []
    for board in inp:
        boards.append(np.array([[int(x) for x in line.split()] for line in board.split('\n')]))
    return numbers, boards

def part1(numbers, boards):
    for n in numbers:
        for b in boards:
            b[b==n] = -1
            if np.any(np.sum(b, axis=0) == -5) or np.any(np.sum(b, axis=1) == -5):
                return n * b[b != -1].sum()

def part2(numbers, boards):
    for n in numbers:
        remove_inds = []
        for i, b in enumerate(boards):
            b[b==n] = -1
            if np.any(np.sum(b, axis=0) == -5) or np.any(np.sum(b, axis=1) == -5):
                if len(boards) == 1:
                    return n * b[b != -1].sum()
                else:
                    remove_inds.append(i)
        for i in reversed(remove_inds):
            boards.pop(i)

numbers, boards = read_input()
print(part1(numbers, deepcopy(boards)))
print(part2(numbers, boards))