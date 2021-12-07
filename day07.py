import numpy as np

with open('inputs/day07.txt') as f:
    pos = list(map(int, f.read().strip().split(',')))

def part1(pos):
    median = int(np.median(pos))
    return sum(abs(p - median) for p in pos)

def part2(pos):
    best_fuel = float('inf')
    for i in range(max(pos)+1):
        fuel = sum([abs(p-i)*(abs(p-i)+1)/2 for p in pos])
        if fuel < best_fuel:
            best_fuel = fuel
    return int(best_fuel)

print(part1(pos))
print(part2(pos))