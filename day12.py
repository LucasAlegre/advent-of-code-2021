def read_graph(filename='inputs/day12.txt'):
    with open(filename) as f:
        edges = [line.strip() for line in f.readlines()]
    graph = {}
    for e in edges:
        a,b = e.split('-')
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    return graph

def search_part1(graph, n, visited, path, paths):
    path += n + '-'
    if n.islower():
        visited.add(n)
    if n == 'end':
        paths.add(path)
        return
    for ne in graph[n]:
        if ne not in visited:
            search_part1(graph, ne, visited.copy(), path, paths)

def search_part2(graph, n, visited, path, paths, repeated):
    path += n + '-'
    if n.islower():
        visited.add(n)
    if n == 'end':
        paths.add(path)
        return
    for ne in graph[n]:
        if ne not in visited:
            search_part2(graph, ne, visited.copy(), path, paths, repeated)
        elif not repeated and ne != 'start':
            search_part2(graph, ne, visited.copy(), path, paths, True)

def part1(graph):
    paths = set()
    search_part1(graph, 'start', set(), '', paths)
    return len(paths)

def part2(graph):
    paths = set()
    search_part2(graph, 'start', set(), '', paths, False)
    return len(paths)

graph = read_graph()
print(part1(graph))
print(part2(graph))