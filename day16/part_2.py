import heapq

Pos = tuple[tuple[int, int], tuple[int, int]]

def get_neighs(grid: list[list[str]], current: Pos):
    if grid[current[0][0]+current[1][0]][current[0][1]+current[1][1]] != '#':
        yield  ((current[0][0]+current[1][0], current[0][1]+current[1][1]), current[1])
    
    if current[1][0] == 0:
        yield (current[0], (-1, 0))
        yield (current[0], (1, 0))
    else:
        yield (current[0], (0, -1))
        yield (current[0], (0, 1))

def get_cost(cur: Pos, neigh: Pos) -> int:
    if cur[1] == neigh[1]:
        return 1
    else:
        return 1000

def dij(grid: list[list[str]], start: Pos) -> tuple[dict[Pos, list[Pos]], dict[Pos, int]]:
    dist: dict[Pos, int] = dict()
    dist[start] = 0
    came_from: dict[Pos, list[Pos]] = dict()
    queue = [(0, start)]
    visited: set[Pos] = set()
    while len(queue) > 0:
        _, current = heapq.heappop(queue)
        visited.add(current)
        for neigh in get_neighs(grid, current):
            if neigh not in visited:
                d = dist[current] + get_cost(current, neigh)
                if neigh in dist.keys():
                    if d == dist[neigh]:
                        if current not in came_from[neigh]:
                            came_from[neigh].append(current)
                    elif d < dist[neigh]:
                        came_from[neigh] = [current]
                        dist[neigh] = d
                else:
                    came_from[neigh] = [current]
                    dist[neigh] = d
                heapq.heappush(queue, (dist[neigh], neigh))
    return (came_from, dist)

def get_s_paths(came_from: dict[Pos, list[Pos]], current: Pos, start: Pos) -> set[tuple[int, int]]:
    out: set[Pos] = set()
    out.add(current[0])
    if current == start:
        return out
    for cf in came_from[current]:
        out = out.union(get_s_paths(came_from, cf, start))
    return out

def find_grid(grid: list[list[str]], start_c: str) -> tuple[int, int]:
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == start_c:
                return (i, j)
with open('input.txt', 'r') as file:
    lines = file.readlines()

grid = [[char for char in line.strip()] for line in lines]

start = find_grid(grid, 'S')
end = find_grid(grid, 'E')

print(start)
print(end)

came_from, dist = dij(grid, (start, (0, 1)))


eA = (end, (-1, 0))
eB = (end, (0, 1))
if min(dist[eA], dist[eB]) == dist[eA]:
    source = eA
else:
    source = eB

s_paths = get_s_paths(came_from, source, (start, (0, 1)))
print(s_paths)
for p in s_paths:
    grid[p[0]][p[1]] = 'O'

for r in grid:
    for c in r:
        print(c, end='')
    print()


print(len(s_paths))