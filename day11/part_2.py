from math import exp, ceil
import numpy as np
from functools import cache
with open('input.txt', 'r') as file:
    lines = file.readlines()

stones = lines[0].strip().split()

# rules:
# 0 -> 1
# even digits -> split 2
# multiply by 2024

@cache
def apply_rules(stone: str, iter: int) -> int:
    if iter == 0:
        return 1
    if stone == '0':
        return apply_rules('1', iter-1)
    if len(stone) % 2 == 0:
        return apply_rules(stone[:len(stone)//2], iter-1) + apply_rules(str(int(stone[len(stone)//2:])), iter-1)
    return apply_rules(str(int(stone)*2024), iter - 1)

result= 0

for stone in stones:
    result += apply_rules(stone, 75)

print(result)