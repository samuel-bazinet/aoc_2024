
from itertools import permutations
from functools import cache
from typing import Literal

Loc = tuple[int, int]

def in_ans(input: str) -> int:
    return int(input[:-1])

@cache
def get_path(target: str) -> list[str]:
    if target == 'A':
        return ['']
    else:
        s = target[0]
        e = target[1]
        pot_sol = []
        for p in paths[(s, e)]:
            #print(s, e, p)
            for s in get_path(target[1:]):
                pot_sol.append(p+s)

    return pot_sol

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
    out = []
    if x < 0:
        x = -x
        p += '<'*x
        x = 0
    if y < 0:
        y = -y
        p += '^'*y
        y = 0
    if y > 0:
        p += 'v'*y
    if x > 0:
        p += '>'*x
    for op in permutations(p):
        if op not in out:
            if validate(op, locs, start):
                out.append(''.join(op) + 'A')
    return out

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

paths = {}
for s in rs:
    for e in rs:
        paths[(s, e)] = get_paths(s, e, r_locs)
for s in ns:
    for e in ns:
        paths[(s, e)] = get_paths(s, e, n_locs)
    
result = 0

@cache
def get_best(sub: str) -> str:
    pot_sols = get_path('A'+sub+'A')
    bps, bp = inner(pot_sols)
    out = pot_sols[bps.index(bp)]
    return out

def inner(pot_sols : list[str]) -> tuple[list[str], str]:
    bps = []
    for s in pot_sols:
        ps2 = get_path('A'+s+'A')
        bp = ps2[0]
        for p in ps2:
            if len(p) < len(bp):
                bp = p
        bps.append(bp)
    bp = bps[0]
    for p in bps:
        if len(p) < len(bp):
            bp = p
    return bps,bp

for line in lines:
    a =line 
    for i in range(3):
        sol = ''
        for sub in line.strip().split('A')[:-1]:
            out = get_best(sub)
            sol += out
        line = sol
        #print(line)
    print(a.strip(), len(sol), sol)
    print()
    result += in_ans(a.strip()) * len(sol)

print(result)