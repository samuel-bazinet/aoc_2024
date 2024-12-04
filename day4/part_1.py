
def go_up(coord: tuple[int, int], chars: list[list[str]]) -> int:
    
    return 1 if chars[coord[0]-1][coord[1]] == 'M' and chars[coord[0]-2][coord[1]] == 'A' and chars[coord[0]-3][coord[1]] == 'S' else 0

def go_down(coord: tuple[int, int], chars: list[list[str]]) -> int:
    
    return 1 if chars[coord[0]+1][coord[1]] == 'M' and chars[coord[0]+2][coord[1]] == 'A' and chars[coord[0]+3][coord[1]] == 'S' else 0

def go_left(coord: tuple[int, int], chars: list[list[str]]) -> int:
    
    return 1 if chars[coord[0]][coord[1]-1] == 'M' and chars[coord[0]][coord[1]-2] == 'A' and chars[coord[0]][coord[1]-3] == 'S' else 0

def go_right(coord: tuple[int, int], chars: list[list[str]]) -> int:
    
    return 1 if chars[coord[0]][coord[1]+1] == 'M' and chars[coord[0]][coord[1]+2] == 'A' and chars[coord[0]][coord[1]+3] == 'S' else 0

def go_left_up(coord: tuple[int, int], chars: list[list[str]]) -> int:
    
    return 1 if chars[coord[0]-1][coord[1]-1] == 'M' and chars[coord[0]-2][coord[1]-2] == 'A' and chars[coord[0]-3][coord[1]-3] == 'S' else 0

def go_right_down(coord: tuple[int, int], chars: list[list[str]]) -> int:
    
    return 1 if chars[coord[0]+1][coord[1]+1] == 'M' and chars[coord[0]+2][coord[1]+2] == 'A' and chars[coord[0]+3][coord[1]+3] == 'S' else 0

def go_left_down(coord: tuple[int, int], chars: list[list[str]]) -> int:
    
    return 1 if chars[coord[0]+1][coord[1]-1] == 'M' and chars[coord[0]+2][coord[1]-2] == 'A' and chars[coord[0]+3][coord[1]-3] == 'S' else 0

def go_right_up(coord: tuple[int, int], chars: list[list[str]]) -> int:
    
    return 1 if chars[coord[0]-1][coord[1]+1] == 'M' and chars[coord[0]-2][coord[1]+2] == 'A' and chars[coord[0]-3][coord[1]+3] == 'S' else 0

def find_xmas(start: tuple[int, int], chars: list[list[str]]) -> int:
    count = 0
    if start[0] >= 3:
        count += go_up(start, chars)
        if start[1] >= 3:
            count += go_left_up(start, chars)
        if len(chars[0]) - start[1] >= 4:
            count += go_right_up(start, chars)
    if len(chars) - start[0] >= 4:
        count += go_down(start, chars)
        if start[1] >= 3:
            count += go_left_down(start, chars)
        if len(chars[0]) - start[1] >= 4:
            count += go_right_down(start, chars)
    if start[1] >= 3:
        count += go_left(start, chars)
    if len(chars[0]) - start[1] >= 4:
        count += go_right(start, chars)
    return count


with open('input.txt', 'r') as file:
    lines = file.readlines()

chars = [[c for c in r.strip()] for r in lines]

count = 0

for r, row in enumerate(chars):
    for c, char in enumerate(row):
        if char == 'X':
            count += find_xmas((r, c), chars)

print(count)
