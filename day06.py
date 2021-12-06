from collections import deque

with open('inputs/day06.txt') as f:
    fishes = list(map(int, f.read().strip().split(',')))

def solve(fishes, days):
    fish_per_day = deque([0 for _ in range(8+1)])
    for f in fishes:
        fish_per_day[f] += 1
    for day in range(1, days+1):
        new_fishes = fish_per_day[0]
        fish_per_day.rotate(-1)
        fish_per_day[6] += new_fishes
        fish_per_day[8] = new_fishes
    return sum(fish_per_day)

print(solve(fishes, days=80))
print(solve(fishes, days=256))