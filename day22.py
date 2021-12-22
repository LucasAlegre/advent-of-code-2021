import re

def read_input(filename='inputs/day22.txt'):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    pattern = re.compile(r'(on|off) x=(\d+|-\d+)\.\.(\d+|-\d+),y=(\d+|-\d+)\.\.(\d+|-\d+),z=(\d+|-\d+)\.\.(\d+|-\d+)')    
    steps = [pattern.match(line).groups() for line in lines]
    steps = [(step[0], tuple(map(int, step[1:]))) for step in steps]
    return steps

def part1(steps):
    on = set()
    for s in steps:
        cmd, cube = s
        x_min, x_max, y_min, y_max, z_min, z_max = cube
        if x_min >= -50 and x_max <= 50 and y_min >= -50 and y_max <= 50 and z_min >= -50 and z_max <= 50:
            for x in range(x_min, x_max+1):
                for y in range(y_min, y_max+1):
                    for z in range(z_min, z_max+1):
                        if cmd == 'on':
                            on.add((x,y,z))
                        else:
                            if (x,y,z) in on:
                                on.remove((x,y,z))
    return len(on)

def overlap(c1, c2):
    (x0a, x1a, y0a, y1a, z0a, z1a) = c1
    (x0b, x1b, y0b, y1b, z0b, z1b) = c2
    return x0b <= x1a and x1b >= x0a and y0b <= y1a and y1b >= y0a and z0b <= z1a and z1b >= z0a

def cubes_subtract_gen(c1, c2):
    if not overlap(c1, c2):
        yield c1
    else:
        x0a, x1a, y0a, y1a, z0a, z1a = c1
        x0b, x1b, y0b, y1b, z0b, z1b = c2
        if x0a < x0b:
            yield (x0a, x0b - 1, y0a, y1a, z0a, z1a)
            x0a = x0b
        if x1a > x1b:
            yield (x1b + 1, x1a, y0a, y1a, z0a, z1a)
            x1a = x1b
        if y0a < y0b:
            yield (x0a, x1a, y0a, y0b - 1, z0a, z1a)
            y0a = y0b
        if y1a > y1b:
            yield (x0a, x1a, y1b + 1, y1a, z0a, z1a)
            y1a = y1b
        if z0a < z0b:
            yield (x0a, x1a, y0a, y1a, z0a, z0b - 1)
            z0a = z0b
        if z1a > z1b:
            yield (x0a, x1a, y0a, y1a, z1b + 1, z1a)
            z1a = z1b

def num_cubes(c):
    (x0, x1, y0, y1, z0, z1) = c
    return (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1)

def part2(steps):
    cubes = []
    for s in steps:
        cubes_aux = []
        cmd, cube = s
        for c in cubes:
            cubes_aux.extend(cubes_subtract_gen(c, cube))
        if cmd == 'on':
            cubes_aux.append(cube)
        cubes = cubes_aux
    return sum(num_cubes(c) for c in cubes)

steps = read_input()
print(part1(steps))
print(part2(steps))