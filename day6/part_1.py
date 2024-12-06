
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

with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [[char for char in line.strip()] for line in lines]

for line in lines:
    for char in line:
        print(char, end='')
    print()

pos = find_start(lines)
lines[pos[0]][pos[1]] = 'X'

dir = 'U'
while pos[0] < len(lines) and pos[1] <= len(lines[0]):
    if dir == 'U':
        if pos[0]-1 < 0:
            break
        if lines[pos[0]-1][pos[1]] != '#':
            lines[pos[0]-1][pos[1]] = 'X'
            pos = (pos[0]-1, pos[1])
        else:
            dir = "R"
    elif dir == 'R':
        if pos[1] +1 >= len(lines[0]):
            break
        if lines[pos[0]][pos[1]+1] != '#':
            lines[pos[0]][pos[1]+1] = 'X'
            pos = (pos[0], pos[1]+1)
        else:
            dir = "D"
    elif dir == 'D':
        if pos[0]+1 >= len(lines):
            break
        if lines[pos[0]+1][pos[1]] != '#':
            lines[pos[0]+1][pos[1]] = 'X'
            pos = (pos[0]+1, pos[1])
        else:
            dir = "L"
    elif dir == 'L':
        if pos[1]-1 <0:
            break
        if lines[pos[0]][pos[1]-1] != '#':
            lines[pos[0]][pos[1]-1] = 'X'
            pos = (pos[0], pos[1]-1)
        else:
            dir = "U"
print()
for line in lines:
    for char in line:
        print(char, end='')
    print()
print(count_X(lines))