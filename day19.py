from math import dist
import numpy as np
from itertools import combinations, product, permutations

def read_input(filename='inputs/day19.txt'):
    with open(filename) as f:
        inp = [s for s in f.read().split('\n\n')]
    scanners = []
    for scan in inp:
        scanners.append(np.vstack([list(map(float, s.split(','))) for s in scan.split('\n')[1:]]).astype(int))
    return scanners

def np_to_tuple(a):
    return [tuple(x) for x in a]

def distances(a):
    d = []
    for i,j in combinations(range(len(a)), 2):
        if i != j:
            d.append(np.linalg.norm(a[i] - a[j]))
    return d

def align(ref_scan, sc):
    for i in range(len(ref_scan)):
        for j in range(len(sc)):
            for r in product([-1,1], repeat=3):
                for d in permutations([0,1,2], r=3):
                    aligned_scan = sc[:, d] * r
                    reference = ref_scan[i] - aligned_scan[j]
                    aligned_scan = aligned_scan + reference
                    if len(set(np_to_tuple(ref_scan)).intersection(set(np_to_tuple(aligned_scan)))) >= 12:
                        return aligned_scan, reference

def part1(scanners):
    aligned_scanners = {0: scanners[0]}
    scan_pos = {0: np.array([0,0,0])}
    dists = [distances(s) for s in scanners]
    while len(aligned_scanners) != len(scanners):
        for ref_i, ref_scan in aligned_scanners.copy().items():
            done = False
            for i, sc in enumerate(scanners):
                if i not in aligned_scanners.keys():
                    if len(set(dists[ref_i]).intersection(set(dists[i]))) >= 66:  # 66 = 12 choose 2
                        aligned_scanners[i], scan_pos[i] = align(ref_scan, sc)
                        done = True
                        break
            if done:
                break
    beacons = set()
    for scan in aligned_scanners.values():
        beacons.update(np_to_tuple(scan))
    return len(beacons), scan_pos

def part2(scan_pos):
    return max(np.abs(s1-s2).sum() for s1, s2 in combinations(scan_pos.values(), 2))

scanners = read_input()
pt1, scan_pos = part1(scanners)
print(pt1)
print(part2(scan_pos))