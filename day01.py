with open('inputs/day01.txt') as f:
    measures = [int(line.strip()) for line in f.readlines()]

part1 = sum([a < b for (a, b) in zip(measures, measures[1:])])
print(part1)

part2 = sum([a < b for (a, b) in zip(measures, measures[3:])])
print(part2)
