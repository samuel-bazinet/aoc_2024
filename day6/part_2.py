
with open('input.txt', 'r') as file:
    lines = file.readlines()


def find_start(grid: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == '^':
                return (i, j)

def count_X(grid) -> int:
    result = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 'X':
                result += 1
    return result

def explore(grid, pos) -> bool:
    dir = 'U'
    explored = dict()
    while pos[0] < len(grid) and pos[1] <= len(grid[0]):
        if dir == 'U':
            if pos[0]-1 < 0:
                break
            if grid[pos[0]-1][pos[1]] != '#':
                pos = (pos[0]-1, pos[1])
                if pos not in explored:
                    explored[pos] = ['U']
                else:
                    if 'U' in explored[pos]:
                        return True
                    else:
                        explored[pos].append('U')
            else:
                dir = "R"
        elif dir == 'R':
            if pos[1] +1 >= len(grid[0]):
                break
            if grid[pos[0]][pos[1]+1] != '#':
                pos = (pos[0], pos[1]+1)
                if pos not in explored:
                    explored[pos] = ['R']
                else:
                    if 'R' in explored[pos]:
                        return True
                    else:
                        explored[pos].append('R')
            else:
                dir = "D"
        elif dir == 'D':
            if pos[0]+1 >= len(grid):
                break
            if grid[pos[0]+1][pos[1]] != '#':
                pos = (pos[0]+1, pos[1])
                if pos not in explored:
                    explored[pos] = ['D']
                else:
                    if 'D' in explored[pos]:
                        return True
                    else:
                        explored[pos].append('D')
            else:
                dir = "L"
        elif dir == 'L':
            if pos[1]-1 <0:
                break
            if grid[pos[0]][pos[1]-1] != '#':
                pos = (pos[0], pos[1]-1)
                if pos not in explored:
                    explored[pos] = ['L']
                else:
                    if 'L' in explored[pos]:
                        return True
                    else:
                        explored[pos].append('L')
            else:
                dir = "U"
    return False

with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [[char for char in line.strip()] for line in lines]

for line in lines:
    for char in line:
        print(char, end='')
    print()

start = find_start(lines)
count = 0

for i, row in enumerate(lines):
    for j, char in enumerate(row):
        if char != '#':
            lines[i][j] = '#'
            if explore(lines, start):
                count += 1
            lines[i][j] = '.'


print(count)