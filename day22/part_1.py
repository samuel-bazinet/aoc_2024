from functools import cache

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

result = 0

for line in lines:
    input = int(line.strip())
    for i in range(2000):
        input = process_sn(input)
    result += input
    #print(line.strip(), input)

print(result)