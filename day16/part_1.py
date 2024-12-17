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

def dij(grid: list[list[str]], start: Pos) -> tuple[dict[Pos, Pos], dict[Pos, int]]:
    dist: dict[Pos, int] = dict()
    dist[start] = 0
    came_from: dict[Pos, Pos] = dict()
    queue = [(0, start)]
    visited: set[Pos] = set()
    while len(queue) > 0:
        _, current = heapq.heappop(queue)
        visited.add(current)
        for neigh in get_neighs(grid, current):
            if neigh not in visited:
                dist[neigh] = dist[current] + get_cost(current, neigh)
                came_from[neigh] = current
                heapq.heappush(queue, (dist[neigh], neigh))
    return (came_from, dist)


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


# for r in grid:
#     for c in r:
#         print(c, end='')
#     print()
print(min(dist[(end, (-1, 0))], dist[(end, (0, 1))]))