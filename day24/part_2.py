from itertools import combinations
import sys

def bit_arr_to_int(arr: list[str]) -> int:
    return int(''.join([a[1] for a in reversed(arr)]), 2)

def print_tree(node, tree) -> str:
    if node[0] == 'x' or node[0] == 'y':
        return 
    current = tree[node]
    print_tree(current[0], tree)
    print_tree(current[2], tree)
    print(f'{node}: {current[0]} {current[1]} {current[2]}')
    #return f'({node}: {print_tree(current[0], tree)} {current[1]} {print_tree(current[2], tree)})'

def op(l: str, r: str, ope: str) -> str:
    match ope:
        case 'XOR':
            return '1' if l != r else '0'
        case 'AND':
            return '1' if l == '1' and r == '1' else '0'
        case 'OR':
            return '1' if l == '1' or r == '1' else '0'
        case _:
            print('ERROR')
            return '-1'

with open('input.txt', 'r') as file:
    lines = file.readlines()

ops = False
wires: dict[str, str] = {}
tree: dict[str, tuple[str, str, str]] = {}
to_do = []

for line in lines:
    line = line.strip()
    if len(line.strip()) < 1:
        ops = True
        continue
    if not ops:
        line = line.split(': ')
        wires[line[0]] = line[1]
    else:
        line = line.split(' ')
        to_do.append([line[0], line[2], line[1], line[-1]])
        tree[line[-1]] = (line[0], line[1], line[2])

def operate(to_do: list[tuple[str, str, str, str]], default_wires: dict[str, str]):
    wires = default_wires.copy()
    while len(to_do) > 0:
        line = to_do.pop(0)
        if line[0] not in wires.keys() or line[1] not in wires.keys():
            to_do.append([line[0], line[2], line[1], line[-1]])
        else:
            wires[line[3]] = op(wires[line[0]], wires[line[1]], line[2])
    return wires

f_wires = operate(to_do.copy(), wires)

def get_current(f_wires):
    zs = [(k, v) for k, v in f_wires.items()]
    zs = list(filter(lambda x: x[0][0] == 'z', zs))
    zs.sort(key=lambda x: x[0])
    return bit_arr_to_int(zs)

xs = [(k, v) for k, v in f_wires.items()]
xs = list(filter(lambda x: x[0][0] == 'x', xs))
xs.sort(key=lambda x: x[0])

ys = [(k, v) for k, v in f_wires.items()]
ys = list(filter(lambda x: x[0][0] == 'y', ys))
ys.sort(key=lambda x: x[0])

x = bit_arr_to_int(xs)
y = bit_arr_to_int(ys)
rs = [x[1]+y[1] for x, y in zip(xs, ys)]

expected = x+ y
current = get_current(f_wires)

ans = []


zs = [(k, v) for k, v in f_wires.items()]
zs = list(filter(lambda x: x[0][0] == 'z', zs))
zs.sort(key=lambda x: x[0])

stdout = sys.stdout

for z, res in zip(zs, rs):
    d = 0
    with open(f'{z[0]}.txt', 'w') as sys.stdout:
        print_tree(z[0], tree)

sys.stdout = stdout

print('Expected:', expected)
print('Current:', current)

# lol do it by hand lmao

'''
for pairs in combinations(combinations(range(len(to_do)), 2), 4):
    check = set()
    for l, r in pairs:
        check.add(l)
        check.add(r)
    if len(check) != 8:
        continue
    for l, r in pairs:
        temp = to_do[l][-1]
        to_do[l][-1] = to_do[r][-1]
        to_do[r][-1] = temp
    z = get_current(operate(to_do.copy(), wires))
    #print(to_do[pairs[0][0]], to_do[pairs[0][1]], to_do[pairs[1][0]], to_do[pairs[1][1]], z)
    if z == expected:
        for l, r in pairs:
            ans.append(to_do[l][-1])
            ans.append(to_do[r][-1])
        break
    for l, r in pairs:
        temp = to_do[l][-1]
        to_do[l][-1] = to_do[r][-1]
        to_do[r][-1] = temp

ans.sort()
print(','.join(ans))
'''