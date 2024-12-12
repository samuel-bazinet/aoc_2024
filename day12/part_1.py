
with open('input.txt', 'r') as file:
    lines = file.readlines()
grid = [[char for char in line.strip()] for line in lines]

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
H = len(grid)
W = len(grid[0])

visited: set[tuple[int, int]] = set()

def find_region(grid: list[list[str]], curr: str, loc: tuple[int, int]) -> tuple[int, int]:
    out = [1, 0]
    visited.add(loc)
    for dir in DIRS:
        y = loc[0]+dir[0]
        x = loc[1]+dir[1]
        if H <= y or y < 0 or W <= x or x < 0:
            out[1]+= 1
        else:
            if grid[y][x] == curr and (y, x) not in visited:
                r= find_region(grid, curr, (y, x))
                out[0] += r[0]
                out[1] += r[1]
            elif grid[y][x] != curr:
                out[1] += 1
    return (out[0], out[1])


result = 0

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if (y, x) not in visited:
            (a, p) = find_region(grid, char, (y, x))
            #print(char, a, p)
            result += a*p

print(result)