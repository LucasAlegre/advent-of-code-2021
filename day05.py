import numpy as np
import re

def read_input(filename='inputs/day05.txt'):
    with open(filename) as f:
        inp = [line.strip() for line in f.readlines()]
    regex = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
    lines = []
    for line in inp:
        lines.append([int(x) for x in regex.match(line).groups()])
    return lines

def solve(lines, part2=False):
    max_p = max([x for line in lines for x in line])
    grid = np.zeros((max_p+1, max_p+1))
    for points in lines:
        min_x, max_x = min(points[0], points[2]), max(points[0], points[2])
        min_y, max_y = min(points[1], points[3]), max(points[1], points[3])
        if points[0] == points[2]:
            grid[range(min_y, max_y+1), points[0]] += 1
        elif points[1] == points[3]:
            grid[points[1], range(min_x, max_x+1)] += 1
        elif part2:
            x, y = points[0], points[1]
            inc_x = 1 if points[0] < points[2] else -1
            inc_y = 1 if points[1] < points[3] else -1
            while x != points[2] and y != points[3]:
                grid[y, x] += 1
                x += inc_x
                y += inc_y
            grid[points[3], points[2]] += 1
    return (grid >= 2).sum()

lines = read_input()
print(solve(lines))
print(solve(lines, part2=True))