def read_input(filename='inputs/day10.txt'):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def corrupted(line):
    stack = []
    pairs = {'[':']', '(':')', '{':'}', '<':'>'}
    for char in line:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if pairs[stack[-1]] == char:
                stack.pop(-1)
            else:
                return char
    return False

def incomplete(line):
    stack = []
    pairs = {'[':']', '(':')', '{':'}', '<':'>'}
    for char in line:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            stack.pop(-1)
    completion = ''.join(pairs[char] for char in reversed(stack))
    return completion

def solve(lines):
    points_pt1 = {')':3, ']':57, '}':1197, '>':25137}
    points_pt2 = {')':1, ']':2, '}':3, '>':4}
    total_points_pt1 = 0
    list_points_pt2 = []
    for line in lines:
        c = corrupted(line)
        if c is not False:
            total_points_pt1 += points_pt1[c]
        else:
            completion = incomplete(line)
            points = 0
            for char in completion:
                points *= 5
                points += points_pt2[char]
            list_points_pt2.append(points)

    total_points_pt2 = sorted(list_points_pt2)[len(list_points_pt2)//2]
    print(total_points_pt1)
    print(total_points_pt2)

lines = read_input()
solve(lines)