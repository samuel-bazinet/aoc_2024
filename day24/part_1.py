
def bit_str_to_int(string: str) -> int:
    return int(string, 2)

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
        if line[0] not in wires.keys() or line[1] not in wires.keys():
            to_do.append((line[0], line[2], line[1], line[-1]))
        else:
            wires[line[-1]] = op(wires[line[0]], wires[line[2]], line[1])

while len(to_do) > 0:
    line = to_do.pop(0)
    if line[0] not in wires.keys() or line[1] not in wires.keys():
        to_do.append((line[0], line[2], line[1], line[-1]))
    else:
        wires[line[3]] = op(wires[line[0]], wires[line[1]], line[2])

zs = [(k, v) for k, v in wires.items()]
zs = list(filter(lambda x: x[0][0] == 'z', zs))
zs.sort(key=lambda x: x[0])

answer = bit_str_to_int(''.join([a[1] for a in reversed(zs)]))
print(answer)