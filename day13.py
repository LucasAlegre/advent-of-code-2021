from math import e
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize': (15,3)})

def read_input(filename='inputs/day13.txt'):
    with open(filename) as f:
        dots_inp, inst_inp = f.read().split('\n\n')
    dots = []
    for line in dots_inp.split('\n'):
        x, y = line.split(',')
        dots.append((int(x), int(y)))
    inst = []
    for line in inst_inp.split('\n'):
        axis, n = line.split('=')
        inst.append((axis[-1], int(n)))
    return dots, inst

def solve(dots, inst):
    max_x, max_y = max([t[0] for t in dots]), max([t[1] for t in dots])
    grid = np.zeros((max_y+1, max_x+1), dtype=int)
    for x,y in dots:
        grid[y,x] = 1
    for (axis, n) in inst:
        if axis == 'x':
            half1, half2 = grid[:,:n], grid[:,n+1:]
            if half1.shape[1] > half2.shape[1]:
                half2 = np.hstack((half2, np.zeros((half1.shape[0],half1.shape[1]-half2.shape[1]), dtype=int)))
            elif half1.shape[1] < half2.shape[1]:
                half1 = np.hstack(((np.zeros((half1.shape[0], half2.shape[1]-half1.shape[1]), dtype=int), half1)))
            half2 = np.fliplr(half2)
        elif axis == 'y':
            half1, half2 = grid[:n,:], grid[n+1:, :]
            if half1.shape[0] > half2.shape[0]:
                half2 = np.vstack((half2, np.zeros((half1.shape[0]-half2.shape[0], half1.shape[1]), dtype=int)))
            elif half1.shape[0] < half2.shape[0]:
                half1 = np.vstack((np.zeros((half2.shape[0]-half1.shape[0], half1.shape[1]), dtype=int), half1))           
            half2 = np.flipud(half2)
        grid = half1 | half2
    return grid

dots, inst = read_input()
print(solve(dots, inst[:1]).sum())
grid = solve(dots, inst)
sns.heatmap(grid)
plt.show()
