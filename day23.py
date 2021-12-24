from heapq import heappop, heappush

def read_input(filename='inputs/day23pt1.txt', size=2):
    with open(filename) as f:
        inp = f.readlines()
    sa = tuple(inp[2+i][3] for i in range(size))
    sb = tuple(inp[2+i][5] for i in range(size))
    sc = tuple(inp[2+i][7] for i in range(size))
    sd = tuple(inp[2+i][9] for i in range(size))
    return sa, sb, sc, sd

def can_enter_room(amphod, room, hallway, i):
    amphods = ['A','B','C','D']
    for a in amphods:
        if a != amphod and a in room:
            return False
    if amphod == 'A':
        if i == 0 and hallway[1] != '.':
            return False
        elif i > 3 and any(a != '.' for a in hallway[3:i]):
            return False
        else:
            return True
    elif amphod == 'B':
        if i < 3 and any(a != '.' for a in hallway[i+1:4]):
            return False
        elif i > 5 and any(a != '.' for a in hallway[5:i]):
            return False
        else:
            return True
    elif amphod == 'C':
        if i < 5 and any(a != '.' for a in hallway[i+1:6]):
            return False
        elif i > 7 and any(a != '.' for a in hallway[7:i]):
            return False
        else:
            return True
    elif amphod == 'D':
        if i == 10 and hallway[9] != '.':
            return False
        elif i < 7 and any(a != '.' for a in hallway[i+1:8]):
            return False
        else:
            return True

def energy_enter(hallway, i, sa, sb, sc, sd):
    if hallway[i] == 'A':
        return abs(i - 2) + sa.count('.')
    elif hallway[i] == 'B':
        return 10 * (abs(i - 4) + sb.count('.'))
    elif hallway[i] == 'C':
        return 100 * (abs(i - 6) + sc.count('.'))
    elif hallway[i] == 'D':
        return 1000 * (abs(i - 8) + sd.count('.'))

def possible_hallway_pos(i, hallway):
    not_allowed = [2,4,6,8]
    possible_pos = []
    for j in range(i, 11):
        if j not in not_allowed:
            if hallway[j] == '.':
                possible_pos.append(j)
            else:
                break
    for j in reversed(range(0, i)):
        if j not in not_allowed:
            if hallway[j] == '.':
                possible_pos.append(j)
            else:
                break
    return possible_pos

def next_nodes(sa, sb, sc, sd, hallway):
    if sa == ('A', 'A') and sb == ('B','B') and sc == ('C','C') and sd == ('D','D'):
        return []

    cost = {'A':1,'B':10,'C':100,'D':1000}
    next = []
    # Leave room
    possible_leave_a = possible_hallway_pos(2, hallway)
    if possible_leave_a:
        for i in range(len(sa)):
            if sa[i] != '.':
                new_sa = sa[:i]+ ('.',) + sa[i+1:]
                for p in possible_leave_a:
                    new_hallway = hallway[:p] + (sa[i],) + hallway[p+1:]
                    energy = (i+1 + abs(2 - p)) * cost[sa[i]]
                    state = (new_sa,sb,sc,sd,new_hallway)
                    next.append((energy, state))
                break
    possible_leave_b = possible_hallway_pos(4, hallway)
    if possible_leave_b:
        for i in range(len(sb)):
            if sb[i] != '.':
                new_sb = sb[:i]+ ('.',) + sb[i+1:]
                for p in possible_leave_b:
                    new_hallway = hallway[:p] + (sb[i],) + hallway[p+1:]
                    energy = (i+1 + abs(4 - p)) * cost[sb[i]]
                    state = (sa,new_sb,sc,sd,new_hallway)
                    next.append((energy, state))
                break
    possible_leave_c = possible_hallway_pos(6, hallway)
    if possible_leave_c:
        for i in range(len(sc)):
            if sc[i] != '.':
                new_sc = sc[:i]+ ('.',) + sc[i+1:]
                for p in possible_leave_c:
                    new_hallway = hallway[:p] + (sc[i],) + hallway[p+1:]
                    energy = (i+1 + abs(6 - p)) * cost[sc[i]]
                    state = (sa,sb,new_sc,sd,new_hallway)
                    next.append((energy, state))
                break
    possible_leave_d = possible_hallway_pos(8, hallway)
    if possible_leave_d:
        for i in range(len(sd)):
            if sd[i] != '.':
                new_sd = sd[:i]+ ('.',) + sd[i+1:]
                for p in possible_leave_d:
                    new_hallway = hallway[:p] + (sd[i],) + hallway[p+1:]
                    energy = (i+1 + abs(8 - p)) * cost[sd[i]]
                    state = (sa,sb,sc,new_sd,new_hallway)
                    next.append((energy, state))
                break

    # Enter room
    for i, amphod in enumerate(hallway):
        if amphod != '.':
            new_hallway = hallway[:i] + ('.',) + hallway[i+1:]
            if amphod == 'A' and can_enter_room(amphod, sa, hallway, i):
                idx = sa.count('.') - 1
                new_sa = sa[:idx] + ('A',) + sa[idx+1:]
                energy = energy_enter(hallway, i, sa, sb, sc, sd)
                state = (new_sa, sb, sc, sd, new_hallway)
                next.append((energy, state))
            elif amphod == 'B' and can_enter_room(amphod, sb, hallway, i):
                idx = sb.count('.') - 1
                new_sb = sb[:idx] + ('B',) + sb[idx+1:]
                energy = energy_enter(hallway, i, sa, sb, sc, sd)
                state = (sa, new_sb, sc, sd, new_hallway)
                next.append((energy, state))
            elif amphod == 'C' and can_enter_room(amphod, sc, hallway, i):
                idx = sc.count('.') - 1
                new_sc = sc[:idx] + ('C',) + sc[idx+1:]
                energy = energy_enter(hallway, i, sa, sb, sc, sd)
                state = (sa, sb, new_sc, sd, new_hallway)
                next.append((energy, state))
            elif amphod == 'D' and can_enter_room(amphod, sd, hallway, i):
                idx = sd.count('.') - 1
                new_sd = sd[:idx] + ('D',) + sd[idx+1:]
                energy = energy_enter(hallway, i, sa, sb, sc, sd)
                state = (sa, sb, sc, new_sd, new_hallway)
                next.append((energy, state))
    return next

def djikstra(start_node, end_node):
    visited = set()
    weights = dict()
    queue = []
    path = {}
    weights[start_node] = 0
    heappush(queue, (0, start_node))
    while len(queue) > 0:
        g, u = heappop(queue)
        visited.add(u)
        for cost, n in next_nodes(*u):
            if n not in visited:
                f = g + cost
                if n not in weights or f < weights[n]:
                    weights[n] = f
                    path[n] = (u, cost)
                    heappush(queue, (f, n))
    return weights[end_node]

def part1(sa, sb, sc, sd):
    hallway = tuple(tuple('.' for _ in range(11)))
    start_node = (sa, sb, sc, sd, hallway)
    end_node = (('A','A'),('B','B'),('C','C'),('D','D'), hallway)
    return djikstra(start_node, end_node)

def part2(sa, sb, sc, sd):
    hallway = tuple(tuple('.' for _ in range(11)))
    start_node = (sa, sb, sc, sd, hallway)
    end_node = (('A','A','A','A'),('B','B','B','B'),('C','C','C','C'),('D','D','D','D'), hallway)
    return djikstra(start_node, end_node)

sa, sb, sc, sd = read_input()
print(part1(sa, sb, sc, sd))
sa, sb, sc, sd = read_input(filename='inputs/day23pt2.txt', size=4)
print(part2(sa, sb, sc, sd))