from functools import cache
from itertools import islice

def window(seq, n=2):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

@cache
def process_sn(input: int) -> int:
    r = input *64
    input = r ^ input
    input %= 16777216
    r = input//32
    input = r ^ input
    input %= 16777216
    r = input*2048
    input = r ^ input
    input %= 16777216
    return input


with open('input.txt', 'r') as file:
    lines = file.readlines()

diffs: list[int] = []
seq: dict[tuple[int, int, int, int], dict[int, int]] = {}

for line in lines:
    diffs: list[int] = []
    input = int(line.strip())
    l = int(line.strip())
    init = input % 10
    for i in range(2000):
        input = process_sn(input)
        current = input % 10
        diffs.append(current - init)
        if i > 2:
            d = (diffs[i-3], diffs[i-2], diffs[i-1], diffs[i])
            #if d == (-2, 1, -1, 3):
                #print(l, current)
            if d not in seq.keys():
                seq[d] = {}
                seq[d][l] = current
            elif l not in seq[d]:
                seq[d][l] = current
        init = current

result = 0

for d, l in seq.items():
    #print(d, l.items(), sum(l.values()))
    r = sum(l.values())
    result = max(r, result)


print(result)