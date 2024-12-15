def find_start(grid: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == '@':
                return (i, j)
    return (-1, -1)

def move(grid: list[list[str]], action: str, loc: tuple[int, int]) -> tuple[int, int]:
    print(grid[loc[0]][loc[1]])
    match action:
        case '^':
            if grid[loc[0]-1][loc[1]] == "#":
                return loc
            elif grid[loc[0]-1][loc[1]] == 'O':
                move(grid, action, (loc[0]-1, loc[1]))

            # use if instead of elif so that I can reuse logic
            if grid[loc[0]-1][loc[1]] == '.':
                grid[loc[0]-1][loc[1]] = grid[loc[0]][loc[1]]
                grid[loc[0]][loc[1]] = '.'
                return (loc[0]-1,loc[1])
            
            return loc
        
        case '>':
            if grid[loc[0]][loc[1]+1] == "#":
                return loc
            elif grid[loc[0]][loc[1]+1] == 'O':
                move(grid, action, (loc[0], loc[1]+1))

            # use if instead of elif so that I can reuse logic
            if grid[loc[0]][loc[1]+1] == '.':
                grid[loc[0]][loc[1]+1] = grid[loc[0]][loc[1]]
                grid[loc[0]][loc[1]] = '.'
                return (loc[0], loc[1]+1)
            return loc
        
        case '<':
            if grid[loc[0]][loc[1]-1] == "#":
                return loc
            elif grid[loc[0]][loc[1]-1] == 'O':
                move(grid, action, (loc[0], loc[1]-1))

            # use if instead of elif so that I can reuse logic
            if grid[loc[0]][loc[1]-1] == '.':
                grid[loc[0]][loc[1]-1] = grid[loc[0]][loc[1]]
                grid[loc[0]][loc[1]] = '.'
                return (loc[0], loc[1]-1)
            
            return loc
        
        case 'v':
            if grid[loc[0]+1][loc[1]] == "#":
                return loc
            elif grid[loc[0]+1][loc[1]] == 'O':
                move(grid, action, (loc[0]+1, loc[1]))

            # use if instead of elif so that I can reuse logic
            if grid[loc[0]+1][loc[1]] == '.':
                grid[loc[0]+1][loc[1]] = grid[loc[0]][loc[1]]
                grid[loc[0]][loc[1]] = '.'
                return (loc[0]+1, loc[1])
            return loc
    return loc

with open('input.txt', 'r') as file:
    lines = file.readlines()

grid = []
actions = ""
p_grid = True

for line in lines:
    
    if len(line.strip()) == 0:
        p_grid = False
        continue
    if p_grid:
        grid.append([c for c in line.strip()])
    else:
        actions += line.strip()

start = find_start(grid)
current = start
for action in actions:
    current = move(grid, action, current)
    '''
    print(action)
    for row in grid:
        for c in row:
            print(c, end='')
        print()
    '''

result = 0

for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == 'O':
            result += i*100+j

print(result)