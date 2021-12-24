def read_input(filename='inputs/day24.txt'):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def run(z, w, c1, c2):
    x = (z % 26 + c1) != w
    if c1 < 0:
        z //= 26
    y = 25*x + 1
    z *= y
    y = (w + c2) * x
    z += y
    return z

def part1(pairs):
    zs = {0: ()}
    CAP = 26**5
    for c1, c2 in pairs:
        new_zs = {}
        for z, v in zs.items():
            for w in range(1, 10):
                if z <= CAP:
                    new_zs[run(z, w, c1, c2)] = v + (w,)
        zs = new_zs
    print("".join(str(c) for c in zs[0]))

def part2(pairs):
    zs = {0: ()}
    CAP = 26**5
    for c1, c2 in pairs:
        new_zs = {}
        for z, v in zs.items():
            for w in reversed(range(1, 10)):
                if z <= CAP:
                    new_zs[run(z, w, c1, c2)] = v + (w,)
        zs = new_zs
    print("".join(str(c) for c in zs[0]))

lines = read_input()
pairs = [(int(lines[i*18 + 5][6:]), int(lines[i*18 + 15][6:])) for i in range(14)]
part1(pairs)
part2(pairs)