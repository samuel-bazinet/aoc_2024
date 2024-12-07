from itertools import product

with open('input.txt', 'r') as file:
    lines = file.readlines()

OPERATORS = ['+', '*']

def verify_ops(result: int, operands: list[int]) -> bool:
    opss = product(OPERATORS, repeat=len(operands)-1)
    for ops in opss:
        v = operands[0]
        for i in range(len(operands)-1):
            if ops[i] == '+':
                v += operands[i+1]
            else:
                v *= operands[i+1]
        if v == result:
            return True
    return False 
        

        

out = 0

for line in lines:
    line = line.strip().split(':')
    result = int(line[0])
    operands = [int(a) for a in line[1].strip().split(' ')]
    if verify_ops(result, operands):
        out += result

print(out)
