from dataclasses import dataclass
from math import ceil, floor
from copy import deepcopy

def read_trees(filename='inputs/day18.txt'):
    with open(filename) as f:
        lines = [eval(line) for line in f.readlines()]
    return [build_tree(l) for l in lines]

@dataclass
class Node:
    number: int
    def __hash__(self) -> int:
        return hash(self.number)

def build_tree(line):
    if type(line) is int:
        return Node(line)
    return (build_tree(line[0]), build_tree(line[1]))

flatten = lambda l: sum(map(flatten, l), []) if type(l) == tuple else [l]

def explode(tree):
    i = 0
    flat = flatten(tree)
    done = False
    def explode_aux(tree, flat, depth=0):
        nonlocal i, done
        if isinstance(tree, Node):
            i += 1
            return tree
        l, r = tree
        if isinstance(l, Node) and isinstance(r, Node):
            if depth >= 4 and not done:
                if i > 0:
                    flat[i-1].number += flat[i].number
                if i + 1 < len(flat) - 1:
                    flat[i+2].number += flat[i+1].number
                done = True
                return Node(0)
        return (explode_aux(l, flat, depth + 1), explode_aux(r, flat, depth + 1))
    return explode_aux(tree, flat)

def split(tree):
    splitted = False
    def split_aux(tree):
        nonlocal splitted
        if isinstance(tree, Node):
            if tree.number >= 10 and not splitted:
                splitted = True
                return (Node(floor(tree.number/2)), Node(ceil(tree.number/2)))
            return tree
        l, r = tree
        return (split_aux(l), split_aux(r))
    return split_aux(tree)

def reduced(tree):
    while True:
        new = explode(tree)
        if new != tree:
            tree = new
            continue
        new = split(tree)
        if new != tree:
            tree = new
            continue
        break
    return tree

def sum_trees(num1, num2):
    s = (num1, num2)
    return reduced(s)

def magnitude(tree):
    if isinstance(tree, Node):
        return tree.number
    l, r = tree
    return 3*magnitude(l) + 2*magnitude(r)

def part1(trees):
    result = trees[0]
    for tree in trees[1:]:
        result = sum_trees(result, tree)
    return magnitude(result)

def part2(trees):
    max_m = 0
    for i, t1 in enumerate(trees):
        for j, t2 in enumerate(trees):
            if i != j:
                max_m = max(max_m, magnitude(sum_trees(deepcopy(t1), deepcopy(t2))))
    return max_m

trees = read_trees()
print(part1(deepcopy(trees)))
print(part2(trees))