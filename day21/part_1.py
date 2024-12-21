
from itertools import permutations, combinations_with_replacement

Loc = tuple[int, int]

def in_ans(input: str) -> int:
    return int(input[:-1])

def get_path(grid: list[list[str]], target: str, loc: dict[str, Loc], final: bool = False) -> str:
    out = ''
    start = loc['A']
    g_type = len(grid)
    for p, char in enumerate(target):
        if char == ' ':
            continue
        t = loc[char]
        y = t[0] - start[0]
        x = t[1] - start[1]
        if g_type == 2 and y == 1 and x == -2:
            out += '<v<A'
            start = t
            continue
        if y == -2 and x == -2 and start[0] != 3:
            out += "<<^^A"
            start = t
            continue
        if g_type == 2:
            while y > 0:
                out += 'v'
                y -= 1
            while x < 0:
                out += '<'
                x += 1
            while x > 0:
                out += '>'
                x -= 1
            while y < 0:
                out += '^'
                y += 1
        else:
            while y < 0:
                out += '^'
                y += 1
            while x < 0:
                out += '<'
                x += 1
            while x > 0:
                out += '>'
                x -= 1
            while y > 0:
                out += 'v'
                y -= 1
        out += 'A'
        start = t
    #print(out)
    return out

def get_locs(grid: list[list[str]]) -> dict[str, Loc]:
    out : dict[str, Loc] = dict()
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            out[char] = (y, x)
    return out

def validate(path: str, locs, start: str) -> bool:
    start = locs[start]
    invalid = locs['']
    for char in path:
        if start == invalid:
            return False
        match char:
            case '<':
                start = (start[0], start[1]-1)
            case '>':
                start = (start[0], start[1]+1)
            case '^':
                start = (start[0]-1, start[1])
            case 'v':
                start = (start[0]+1, start[1])
    return True

def get_paths(start: str, end: str, locs: dict[str, Loc]) -> list[str]:
    s = locs[start]
    e = locs[end]
    y = e[0] - s[0]
    x = e[1] - s[1]
    p = ''
    out = set()
    if y < 0:
        y = -y
        p += '^'*y
    else:
        p += 'v'*y
    if x < 0:
        x = -x
        p += '<'*x
    else:
        p += '>'*x
    for op in permutations(p):
        if op not in out:
            if validate(op, locs, start):
                out.add(''.join(op))
    return list(out)

def run(sequence: str, grid: list[list[str]]) -> str:
    start = get_locs(grid)['A']
    out = ''
    for char in sequence:
        match char:
            case '<':
                start = (start[0], start[1]-1)
            case '>':
                start = (start[0], start[1]+1)
            case '^':
                start = (start[0]-1, start[1])
            case 'v':
                start = (start[0]+1, start[1])
            case 'A':
                out += grid[start[0]][start[1]]
    return out

with open('input.txt', 'r') as file:
    lines = file.readlines()

rs = ['^', 'v', 'A', '<', '>']
ns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A']

r_grid = [['', '^', 'A'], ['<', 'v', '>']]
r_locs = get_locs(r_grid)
n_grid = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['', '0', 'A']]
n_locs = get_locs(n_grid)

r_paths = { (s, e):get_paths(s, e, r_locs) for s, e in combinations_with_replacement(rs, 2)}
print(r_paths)
n_paths = { (s, e):get_paths(s, e, n_locs) for s, e in combinations_with_replacement(ns, 2)}
print(n_paths)
result = 0

for line in lines:
    r = get_path(r_grid, get_path(r_grid, get_path(n_grid, line.strip(), n_locs), r_locs), r_locs, True)
    #print(r)
    #print(len(r), in_ans(line.strip()), len(r)*in_ans(line.strip()))
    result += len(r)*in_ans(line.strip())
    #print()
'''
test = '<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'

a = run(test, r_grid)
b = run(a, r_grid)
c = run(b, n_grid)

print(c)
print(b)
print(a)
print(test)
'''
print(result)