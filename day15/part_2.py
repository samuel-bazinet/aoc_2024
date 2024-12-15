from copy import deepcopy
from time import sleep

def find_start(grid: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == '@':
                return (i, j)
    return (-1, -1)

def check_vert(grid: list[list[str]], action: str, loc: tuple[int, int], current: str, depth: int = 0) -> bool:
    
    match action:
        case '^':
            if current == '[':
                if grid[loc[0]-1][loc[1]] != '#' and grid[loc[0]-1][loc[1]+1] != '#':
                    ret_val = True
                    if grid[loc[0]-1][loc[1]] in '[]':
                        ret_val = check_vert(grid, action, (loc[0]-1, loc[1]), grid[loc[0]-1][loc[1]], depth+1)
                    if ret_val and grid[loc[0]-1][loc[1]+1] in '[]':
                        ret_val = check_vert(grid, action, (loc[0]-1, loc[1]+1), grid[loc[0]-1][loc[1]+1], depth+1)
                    return ret_val
                else:
                    return False
            elif current == ']':
                if grid[loc[0]-1][loc[1]] != '#' and grid[loc[0]-1][loc[1]-1] != '#':
                    ret_val = True
                    if grid[loc[0]-1][loc[1]] in '[]':
                        ret_val = check_vert(grid, action, (loc[0]-1, loc[1]), grid[loc[0]-1][loc[1]], depth+1)
                    if ret_val and grid[loc[0]-1][loc[1]-1] in '[]':
                        ret_val = check_vert(grid, action, (loc[0]-1, loc[1]-1), grid[loc[0]-1][loc[1]-1], depth+1)
                    return ret_val
                else:
                    return False
        case 'v':
            if current == '[':
                if grid[loc[0]+1][loc[1]] != '#' and grid[loc[0]+1][loc[1]+1] != '#':
                    ret_val = True
                    if grid[loc[0]+1][loc[1]] in '[]':
                        ret_val = check_vert(grid, action, (loc[0]+1, loc[1]), grid[loc[0]+1][loc[1]], depth+1)
                    if ret_val and grid[loc[0]+1][loc[1]+1] in '[]':
                        ret_val = check_vert(grid, action, (loc[0]+1, loc[1]+1), grid[loc[0]+1][loc[1]+1], depth+1)
                    return ret_val
                else:
                    return False
            elif current == ']':
                if grid[loc[0]+1][loc[1]] != '#' and grid[loc[0]+1][loc[1]-1] != '#':
                    ret_val = True
                    if grid[loc[0]+1][loc[1]] in '[]':
                        ret_val = check_vert(grid, action, (loc[0]+1, loc[1]), grid[loc[0]+1][loc[1]], depth+1)
                    if ret_val and grid[loc[0]+1][loc[1]-1] in '[]':
                        ret_val = check_vert(grid, action, (loc[0]+1, loc[1]-1), grid[loc[0]+1][loc[1]-1], depth+1)
                    return ret_val
                else:
                    return False
    print("huh")
    return False

def check_horz(grid: list[list[str]], action: str, loc: tuple[int, int], depth: int = 0) -> bool:
    
    match action:
        case '<':
            if grid[loc[0]][loc[1]-1] == ']':
                return check_horz(grid, action, (loc[0], loc[1]-1), depth + 1)
            elif grid[loc[0]][loc[1]-1] == '[':
                return check_horz(grid, action, (loc[0], loc[1]-1), depth)
            elif grid[loc[0]][loc[1]-1] == '#':
                return False
            return True
        case '>':
            if grid[loc[0]][loc[1]+1] == '[':
                return check_horz(grid, action, (loc[0], loc[1]+1), depth + 1)
            elif grid[loc[0]][loc[1]+1] == ']':
                return check_horz(grid, action, (loc[0], loc[1]+1), depth)
            elif grid[loc[0]][loc[1]+1] == '#':
                return False
            return True
    print('huh')
    return False

def move(grid: list[list[str]], action: str, loc: tuple[int, int]) -> tuple[int, int]:
    match action:
        case '^':
            if grid[loc[0]-1][loc[1]] == "#":
                return loc
            elif grid[loc[0]-1][loc[1]] == '[':
                if check_vert(grid, action, (loc[0]-1, loc[1]), '['):
                    move(grid, action, (loc[0]-1, loc[1]))
                    move(grid, action, (loc[0]-1, loc[1]+1))
            elif grid[loc[0]-1][loc[1]] == ']':
                if check_vert(grid, action, (loc[0]-1, loc[1]), ']'):
                    move(grid, action, (loc[0]-1, loc[1]))
                    move(grid, action, (loc[0]-1, loc[1]-1))

            # use if instead of elif so that I can reuse logic
            if grid[loc[0]-1][loc[1]] == '.':
                grid[loc[0]-1][loc[1]] = grid[loc[0]][loc[1]]
                grid[loc[0]][loc[1]] = '.'
                return (loc[0]-1,loc[1])
            
            return loc
        
        case '>':
            if grid[loc[0]][loc[1]+1] == "#":
                return loc
            elif grid[loc[0]][loc[1]+1] == '[' or grid[loc[0]][loc[1]+1] == ']':
                if check_horz(grid, action, (loc[0], loc[1]+1)):
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
            elif grid[loc[0]][loc[1]-1] == '[' or grid[loc[0]][loc[1]-1] == ']':
                if check_horz(grid, action, (loc[0], loc[1]-1)):
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
            elif grid[loc[0]+1][loc[1]] == '[':
                if check_vert(grid, action, (loc[0]+1, loc[1]), '['):
                    move(grid, action, (loc[0]+1, loc[1]))
                    move(grid, action, (loc[0]+1, loc[1]+1))
            elif grid[loc[0]+1][loc[1]] == ']':
                if check_vert(grid, action, (loc[0]+1, loc[1]), ']'):
                    move(grid, action, (loc[0]+1, loc[1]))
                    move(grid, action, (loc[0]+1, loc[1]-1))

            # use if instead of elif so that I can reuse logic
            if grid[loc[0]+1][loc[1]] == '.':
                grid[loc[0]+1][loc[1]] = grid[loc[0]][loc[1]]
                grid[loc[0]][loc[1]] = '.'
                return (loc[0]+1, loc[1])
            return loc
    print('huhuh')
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
        g_line = []
        for c in line:
            if c == '.':
                g_line.extend(['.', '.'])
            elif c == 'O':
                g_line.extend(['[', ']'])
            elif c == '#':
                g_line.extend(['#', '#'])
            elif c == '@':
                g_line.extend(['@', '.'])
        grid.append(g_line)
    else:
        actions += line.strip()

for row in grid:
        for c in row:
            print(c, end='')
        print()

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
    #sleep(0.1)
    '''

    

result = 0
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == '[':
            result += i*100+j

print(result)
