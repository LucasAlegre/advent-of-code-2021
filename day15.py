import heapq as hq
import math
import numpy as np

def read_map(filename='inputs/day15.txt'):
    with open(filename) as f:
        lines = [[int(c) for c in line.strip()] for line in f.readlines()]
    return np.array(lines)

def neighbors(map, x, y):
    n = []
    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        if dx+x >= 0 and dx+x < map.shape[0] and dy+y >= 0 and dy+y < map.shape[1]:
            n.append((dx+x, dy+y))
    return n

def part1(map):
    start_node = (0, 0)
    end_node = (len(map)-1, len(map[0])-1)
    visited = set()
    weights = {(x,y): math.inf for x in range(map.shape[0]) for y in range(map.shape[1])}
    path = {}
    queue = []
    weights[start_node] = 0
    hq.heappush(queue, (0, start_node))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        visited.add(u)
        for n in neighbors(map, *u):
            if n not in visited:
                f = g + map[n[0],n[1]]
                if f < weights[n]:
                    weights[n] = f
                    path[n] = u
                    hq.heappush(queue, (f, n))
    return weights[end_node]

def part2(map):
    map_c = map.copy()
    for _ in range(4):
        map_c = map_c + 1
        map_c = np.where(map_c > 9, 1, map_c)
        map = np.hstack((map, map_c))
    map_c = map.copy()
    for _ in range(4):
        map_c = map_c + 1
        map_c = np.where(map_c > 9, 1, map_c)
        map = np.vstack((map, map_c))
    return part1(map)

map = read_map()
print(part1(map))
print(part2(map))
