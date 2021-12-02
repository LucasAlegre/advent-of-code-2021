with open('inputs/day02.txt') as f:
    commands = [line.strip().split() for line in f.readlines()]

def part1(commands):
    pos = [0, 0]
    for (c, n) in commands:
        n = int(n)
        if c == 'forward':
            pos[0] += n
        elif c == 'down':
            pos[1] += n
        elif c == 'up':
            pos[1] -= n
    return pos[0] * pos[1]

def part2(commands):
    pos = [0, 0, 0]
    for (c, n) in commands:
        n = int(n)
        if c == 'forward':
            pos[0] += n
            pos[1] += pos[2] * n
        elif c == 'down':
            pos[2] += n
        elif c == 'up':
            pos[2] -= n
    return pos[0] * pos[1]

print(part1(commands))
print(part2(commands))
