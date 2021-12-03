import numpy as np

with open('inputs/day03.txt') as f:
    report = [line.strip() for line in f.readlines()]
    numbers = np.array([[int(x) for x in line] for line in report])

def bin_to_dec(bin_array):
    return sum([int(x*2**(bin_array.shape[0]-i-1)) for i,x in enumerate(bin_array)])

def part1(numbers):
    gamma = np.count_nonzero(numbers, axis=0)
    gamma = np.where(gamma >= numbers.shape[0]/2, 1, 0)
    epsilon = 1 - gamma
    gamma = bin_to_dec(gamma)
    epsilon = bin_to_dec(epsilon)
    return gamma * epsilon

def part2(numbers):
    l = numbers.copy()
    for i in range(numbers.shape[1]):
        count = np.count_nonzero(l[:,i])
        most_common = int(count >= l.shape[0]/2)
        l = l[np.where(l[:,i] == most_common)]
        if l.shape[0] == 1:
            break
    oxygem = bin_to_dec(l[0])
    
    l = numbers.copy()
    for i in range(numbers.shape[1]):
        count = np.count_nonzero(l[:,i])
        least_common = 1 - int(count >= l.shape[0]/2)
        l = l[np.where(l[:,i] == least_common)]
        if l.shape[0] == 1:
            break
    co2 = bin_to_dec(l[0])
    return oxygem * co2

print(part1(numbers))
print(part2(numbers))