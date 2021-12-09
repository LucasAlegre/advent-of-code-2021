import math

def read_map(filename='inputs/day09.txt'):
    with open(filename) as f:
        map = [line.strip() for line in f.readlines()]
    return map

def low_points(map):
    low_points = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            lowest = True
            for d in [(0,1), (0,-1), (1,0), (-1,0)]:
                x, y = i + d[0], j + d[1]
                if x < 0 or x >= len(map) or y < 0 or y >= len(map[0]):
                    continue
                if map[i][j] >= map[x][y]:
                    lowest = False
                    break
            if lowest:
                low_points.append((i,j))
    return low_points

def compute_basin(map, point, basin):
    basin.add(point)
    for d in [(0,1), (0,-1), (1,0), (-1,0)]:
        x, y = point[0] + d[0], point[1] + d[1]
        if x < 0 or x >= len(map) or y < 0 or y >= len(map[0]):
            continue
        if int(map[x][y]) != 9 and (x,y) not in basin:
            compute_basin(map, (x,y), basin)
    return basin

def part1(map):
    risk_level = 0
    for i, j in low_points(map):
        risk_level += 1 + int(map[i][j])
    return risk_level

def part2(map):
    points = low_points(map)
    basins = [compute_basin(map, p, set()) for p in points]
    basins.sort(key=len)
    return math.prod(len(b) for b in basins[-3:])

map = read_map()
print(part1(map))
print(part2(map))