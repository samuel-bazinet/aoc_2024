
from dataclasses import dataclass
from sympy import symbols, Eq, solve

@dataclass
class Input:
    ax: int
    ay: int
    bx: int
    by: int
    x: int
    y: int

    def __repr__(self):
        return f'Ax: {self.ax}, Ay: {self.ay}, Bx: {self.bx}, By: {self.by}, X: {self.x}, Y: {self.y}'

def line_to_useful(lines: list[str]) -> list[Input]:
    a = (0, 0)
    b = (0, 0)
    p = (0, 0)
    out: list[Input] = []
    for line in lines:
        if line[0] == 'B':
            if line[7] == 'A':
                line = line.strip().split(' ')
                a = (int(line[-2][2:-1]), int(line[-1][2:]))
            elif line[7] == 'B':
                line = line.strip().split(' ')
                b = (int(line[-2][2:-1]), int(line[-1][2:]))
        elif line[0] == 'P':
            line = line.strip().split(' ')
            p = (int(line[-2][2:-1]), int(line[-1][2:]))
            out.append(Input(a[0], a[1], b[0], b[1], p[0]+10000000000000, p[1] + 10000000000000))
    return out

def check_if_solveable(input: Input) -> int:
    a, b = symbols('a,b')
    eq1 = Eq((input.ax*a+input.bx*b), input.x)
    eq2 = Eq((input.ay*a+input.by*b), input.y)
    r = solve((eq1, eq2), (a, b))
    if len(r) != 0:
        if int(r[a]) == r[a] and int(r[b]) == r[b]:
            return 3*r[a]+r[b]
    return 0

with open('input.txt', 'r') as file:
    lines = file.readlines()

inputs = line_to_useful(lines)
result = 0
for input in inputs:
    result += check_if_solveable(input)

print(result)