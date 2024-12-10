
DIRS = [(0,1), (1, 0), (-1, 0), (0, -1)]

def explore_grid(current: tuple[int, int], target: int, grid: list[list[int]]) -> list[tuple[int, int]]:
    if target == 10:
        return [current]
    result: list[tuple[int, int]] = []
    h = len(grid)
    w = len(grid[0])
    for dir in DIRS:
        if 0 <=current[0] + dir[0] < h and 0 <= current[1] + dir[1] < w:
            if grid[current[0]+dir[0]][current[1]+dir[1]] == target:
                result.extend(explore_grid((current[0]+dir[0],current[1]+dir[1]), target + 1, grid))
    return result


with open('input.txt', 'r') as file:
    lines = file.readlines()
    grid = [[int(i) for i in line.strip()] for line in lines]

result = 0
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == 0:
            result += len(set(explore_grid((y, x), 1, grid)))

print(result)