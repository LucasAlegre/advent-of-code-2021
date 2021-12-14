import re

def read_input(filename='inputs/day14.txt'):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    polymer = lines[0]
    pattern = re.compile(r'(.*) -> (.*)')
    rules = {}
    for line in lines[2:]:
        a, b = pattern.match(line).groups()
        rules[a] = b
    return polymer, rules

def solve(polymer, rules, steps):
    counter = {}
    count_letter = {}
    for a, b in zip(polymer, polymer[1:]):
        counter[a+b] = counter.get(a+b, 0) + 1
        count_letter[a] = count_letter.get(a, 0) + 1
    count_letter[polymer[-1]] = count_letter.get(polymer[-1], 0) + 1
    
    for _ in range(steps):
        new_counter = counter.copy()
        for key, count in counter.items():
            if key in rules:
                old_value = counter[key]
                new_counter[key[0]+rules[key]] = new_counter.get(key[0]+rules[key], 0) + counter[key]
                new_counter[rules[key]+key[1]] = new_counter.get(rules[key]+key[1], 0) + counter[key]
                new_counter[key] -= old_value
                count_letter[rules[key]] = count_letter.get(rules[key], 0) + count
        counter = new_counter    
    
    return max(count_letter.values()) - min(count_letter.values())
 
polymer, rules = read_input()
print(solve(polymer, rules, 10))
print(solve(polymer, rules, 40))