from functools import cache

@cache
def contains(to_check: str) -> bool:
    ret_val = False
    for t in available:
        if to_check.startswith(t):
            if len(t) == len(to_check):
                return True
            else:
                ret_val = ret_val or contains(to_check[len(t):]) 
    return ret_val

with open('input.txt', 'r') as file:
    lines = file.readlines()

available = lines[0].strip().split(', ')

to_check = [line.strip() for line in lines[2:]]

result = 0

for t in to_check:
    if contains(t):
        #print(t, 'good')
        result += 1

print(result)