from itertools import combinations
import heapq
Pos = tuple[int, int]

def find_grid(target: str, grid: list[list[str]]) -> Pos:
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == target:
                return (y, x)

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

def find_pairs(dists: dict[Pos, int]) -> int:
    result = 0
    pairs = list(combinations(dists.items(), 2))
    for (a, b) in pairs:
        if abs(a[1]-b[1]) - get_dist(a[0], b[0]) >= 100:
            if get_dist(a[0], b[0]) <= 20:
                #print(a, b, abs(a[1]-b[1]) - get_dist(a[0], b[0]))
                result += 1
    return result


with open('input.txt', 'r') as file:
    lines = file.readlines()

grid = [[c for c in line.strip()] for line in lines]

H = len(grid)
W = len(grid[0])

start = find_grid('S', grid)
end = find_grid('E', grid)

_, dist = a_star(grid, start, end)
first = dist[end]
print("First:", first)

result = find_pairs(dist)

print(result)