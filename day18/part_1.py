import heapq
Pos = tuple[int, int]

DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def get_neighs(grid: list[list[str]], current: Pos):
    for dir in DIRS:
        if 0 <= current[0]+dir[0] < H and 0 <= current[1]+dir[1] < W: 
            if grid[current[0]+dir[0]][current[1]+dir[1]] != '#':
                yield  (current[0]+dir[0], current[1]+dir[1])

def get_cost(cur: Pos, neigh: Pos) -> int:
    return 1

def get_dist(cur: Pos, end: Pos) -> int:
    return abs(cur[0]-end[0]) + abs(cur[1]-end[1])

def a_star(grid: list[list[str]], start: Pos, end: Pos) -> tuple[dict[Pos, Pos], dict[Pos, int]]:
    dist: dict[Pos, int] = dict()
    dist[start] = 0
    came_from: dict[Pos, Pos] = dict()
    queue = [(get_dist(start, end), start)]
    visited: set[Pos] = set()
    while len(queue) > 0:
        _, current = heapq.heappop(queue)
        if current == end:
            return (came_from, dist)
        visited.add(current)
        for neigh in get_neighs(grid, current):
            if neigh not in visited:
                t_score= dist[current] + get_cost(current, neigh)
                if neigh not in dist.keys() or t_score < dist[neigh]:
                    dist[neigh] = t_score
                    came_from[neigh] = current
                    if neigh not in queue:
                        heapq.heappush(queue, (dist[neigh] + get_dist(neigh, end), neigh))
    return (came_from, dist)

with open('input.txt', 'r') as file:
    lines = file.readlines()

H = 71
W = 71


grid: list[list[str]] = [['.' for _ in range(W)] for _ in range(H)]

for i in range(1024):
    line = lines[i].strip().split(',')
    grid[int(line[1])][int(line[0])] = '#'

for r in grid:
    for c in r:
        print(c, end='')
    print()

came_from, costs = a_star(grid, (0, 0), (H-1, W-1))

print(costs[(H-1, W-1)])