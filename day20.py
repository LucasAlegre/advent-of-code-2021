import numpy as np

def read_input(filename='inputs/day20.txt'):
    with open(filename) as f:
        algo, image = f.read().split('\n\n')
    algo = np.array([1 if x == '#' else 0 for x in algo])
    image = np.array([[1 if x == '#' else 0 for x in line] for line in image.split('\n')])
    return algo, image

def step(image, algo):
    result = []
    for i in range(image.shape[0]-2):
        line = []
        for j in range(image.shape[1]-2):
            window = image[i:i+3,j:j+3].flatten()
            num = int(window.dot(1 << np.arange(window.size)[::-1]))
            value = algo[num]
            line.append(value)
        result.append(line)
    return np.vstack(result)

def solve(algo, image, steps):
    image = np.pad(image, 3*50)
    for _ in range(steps):
        image = step(image, algo)
    return image.sum()

algo, image = read_input()
print(solve(algo, image.copy(), steps=2))
print(solve(algo, image, steps=50))