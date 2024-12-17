def find_a(start, seq, step):
    if step == len(seq):
        return start//8
    for a in range(start, (start+8)*2):
        b = a % 8
        b = b ^ 1
        c = a//(2**b)
        b = b ^ 5
        b = b ^ c
        if b % 8 == seq[-(step+1)]:
            if ops(seq, a, 0, 0) == seq[-(step+1) if step < len(seq) else 0:]:
                return find_a(a*8, seq, step+1)

def get_comb(operand: int, A: int, B: int, C: int) -> int:
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case _:
            print("ERROR:", operand)

def ops(operators: list[int], A: int, B: int, C: int) -> list[int]:
    pointer = 0
    out = []
    while pointer < len(operators):
        j = False
        match operators[pointer]:
            case 0:
                A = int(A/(2**get_comb(operators[pointer+1], A, B, C)))
            case 1:
                B = B ^ operators[pointer+1]
            case 2:
                B = get_comb(operators[pointer+1], A, B, C)%8
            case 3:
                if A != 0:
                    pointer = operators[pointer+1]
                    j = True
            case 4:
                B = B ^ C
            case 5:
                out.append(get_comb(operators[pointer+1], A, B, C)%8)
                
            case 6:
                B = int(A/(2**get_comb(operators[pointer+1], A, B, C)))
            case 7:
                C = int(A/(2**get_comb(operators[pointer+1], A, B, C)))
            case _:
                print("ERROR:", operators[pointer])
        if not j:
            pointer += 2
    return out

with open('input.txt', 'r') as file:
    lines = file.readlines()

A = int(lines[0].strip().split(' ')[-1])
B = int(lines[1].strip().split(' ')[-1])
C = int(lines[2].strip().split(' ')[-1])

program = [int(i) for i in lines[4].strip().split(' ')[-1].split(',')]

a = 0
a = find_a(a, program, 0)
print(a)
print(ops(program, a, 0, 0))