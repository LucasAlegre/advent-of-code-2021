import re

def read_target(filename='inputs/day17.txt'):
    with open(filename) as f:
        line = f.read().strip()
    x_min, x_max, y_min, y_max = map(int, re.match(r'target area: x=(\d+|-\d+)\.\.(\d+|-\d+), y=(\d+|-\d+)\.\.(\d+|-\d+)', line).groups())
    return x_min, x_max, y_min, y_max

def run(x_min, x_max, y_min, y_max, x_vel, y_vel):
    x, y = 0, 0
    max_y = y
    reached_target = False
    while True:
        x += x_vel
        y += y_vel
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        y_vel -= 1
        max_y = max(max_y, y)
        if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
            reached_target = True
            break
        if x == 0 and not (x >= x_min and x <= x_max):
            break
        if y < y_min:
            break
    return reached_target, max_y

def part1(x_min, x_max, y_min, y_max):
    max_y = 0
    for i in range(30):
        for j in range(1000):
            reached_target, y = run(x_min, x_max, y_min, y_max, i, j)
            if reached_target:
                max_y = max(max_y, y)
    return max_y

def part2(x_min, x_max, y_min, y_max):
    total = 0
    for i in range(1000):
        for j in range(y_min, 1000):
            reached_target, y = run(x_min, x_max, y_min, y_max, i, j)
            if reached_target:
                total += 1
    return total

x_min, x_max, y_min, y_max = read_target()
print(part1(x_min, x_max, y_min, y_max))
print(part2(x_min, x_max, y_min, y_max))