

def find_xmas(start: tuple[int, int], chars: list[list[str]]) -> int:
    if start[0] == 0 or start[0] == len(chars)-1 or start[1] == 0 or start[1] == len(chars[0])-1:
        return 0
    if chars[start[0]-1][start[1]-1] == 'M':
        if chars[start[0]-1][start[1]+1] == 'M':
            if chars[start[0]+1][start[1]+1] == 'S' and chars[start[0]+1][start[1]-1] == 'S':
                return 1
        elif chars[start[0]+1][start[1]-1] == 'M':
            if chars[start[0]+1][start[1]+1] == 'S' and chars[start[0]-1][start[1]+1] == 'S':
                return 1
    elif chars[start[0]+1][start[1]+1] == 'M':
        if chars[start[0]-1][start[1]+1] == 'M':
            if chars[start[0]-1][start[1]-1] == 'S' and chars[start[0]+1][start[1]-1] == 'S':
                return 1
        elif chars[start[0]+1][start[1]-1] == 'M':
            if chars[start[0]-1][start[1]-1] == 'S' and chars[start[0]-1][start[1]+1] == 'S':
                return 1
    return 0


with open('input.txt', 'r') as file:
    lines = file.readlines()

chars = [[c for c in r.strip()] for r in lines]

count = 0

for r, row in enumerate(chars):
    for c, char in enumerate(row):
        if char == 'A':
            count += find_xmas((r, c), chars)

print(count)
