from copy import deepcopy

def read_input(filename='inputs/day25.txt'):
    with open(filename) as f:
        map = [[c for c in line.strip()] for line in f.readlines()]
    return map

def part1(map):
    moving = True
    step = 0
    n_row, n_col = len(map), len(map[0])
    while moving:
        step += 1
        moving = False
        new_map = deepcopy(map)
        for i in range(n_row):
            for j in range(n_col):
                if map[i][j] == '>' and map[i][(j+1)%n_col] == '.':
                    new_map[i][(j+1)%n_col] = '>'
                    new_map[i][j] = '.'
                    moving = True
        map = new_map
        new_map = deepcopy(map)
        for i in range(n_row):
            for j in range(n_col):
                if map[i][j] == 'v' and map[(i+1)%n_row][j] == '.':
                    new_map[(i+1)%n_row][j] = 'v'
                    new_map[i][j] = '.'
                    moving = True
        map = new_map
    print(step)
        
map = read_input()
part1(map)