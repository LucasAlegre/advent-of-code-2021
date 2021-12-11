import numpy as np

def read_input(filename='inputs/day11.txt'):
    with open(filename) as f:
        grid = np.array([[int(x) for x in line.strip()] for line in f.readlines()])
    return grid

def run_step(grid):
    grid += 1
    flash = True
    while flash:
        flash = False
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i,j] > 9:
                    flash = True
                    grid[i,j] = -1000
                    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                        if i+dx < grid.shape[0] and i+dx >= 0 and j+dy < grid.shape[1] and j+dy >= 0:
                            grid[i+dx,j+dy] += 1

def solve(grid):
    total_flashes = 0
    first_step_all_flash = None
    for step in range(1, 1000):
        run_step(grid)
        flashes = np.sum(grid < 0)
        if step <= 100:
            total_flashes += flashes
        if flashes == grid.shape[0]*grid.shape[1] and first_step_all_flash is None:
            first_step_all_flash = step
            break
        grid[grid < 0] = 0
    print(total_flashes)
    print(first_step_all_flash)

grid = read_input()
solve(grid)