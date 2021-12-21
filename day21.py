from functools import cache
from itertools import product

def read_input(filename='inputs/day21.txt'):
    with open(filename) as f:
        pos = [int(line.strip().split(': ')[1]) for line in f.readlines()]
    p1, p2 = pos
    return p1, p2

def part1(p1, p2):
    score_1, score_2 = 0, 0
    dice = 1
    rolls = 0
    while True:
        p1 = (p1 + 3*dice+3 - 1) % 10 + 1
        dice += 3
        rolls += 3
        score_1 += p1
        if score_1 >= 1000:
            return score_2 * rolls
        p2 = (p2 + 3*dice+3 - 1) % 10 + 1
        dice += 3
        rolls += 3
        score_2 += p2
        if score_2 >= 1000:
            return score_1 * rolls

@cache
def win_p1(p1, p2, s1, s2, d, p):
    if p == 1:
        n_p1 = (p1 + d  - 1) % 10 + 1
        n_s1 = s1 + n_p1
        if n_s1 >= 21:
            return 1
        else:
            return sum(win_p1(n_p1, p2, n_s1, s2, sum(dices), 2) for dices in product([1,2,3], repeat=3))
    elif p == 2:
        n_p2 = (p2 + d  - 1) % 10 + 1
        n_s2 = s2 + n_p2
        if n_s2 >= 21:
            return 0
        else:
            return sum(win_p1(p1, n_p2, s1, n_s2, sum(dices), 1) for dices in product([1,2,3], repeat=3))

@cache
def win_p2(p1, p2, s1, s2, d, p):
    if p == 1:
        n_p1 = (p1 + d  - 1) % 10 + 1
        n_s1 = s1 + n_p1
        if n_s1 >= 21:
            return 0
        else:
            return sum(win_p2(n_p1, p2, n_s1, s2, sum(dices), 2) for dices in product([1,2,3], repeat=3))
    elif p == 2:
        n_p2 = (p2 + d  - 1) % 10 + 1
        n_s2 = s2 + n_p2
        if n_s2 >= 21:
            return 1
        else:
            return sum(win_p2(p1, n_p2, s1, n_s2, sum(dices), 1) for dices in product([1,2,3], repeat=3))

def part2(p1, p2):
    wins_p1 = sum(win_p1(p1, p2, 0, 0, sum(dices), 1) for dices in product([1,2,3], repeat=3))
    wins_p2 = sum(win_p2(p1, p2, 0, 0, sum(dices), 1) for dices in product([1,2,3], repeat=3))
    return max(wins_p1, wins_p2)

p1, p2 = read_input()
print(part1(p1, p2))
print(part2(p1, p2))