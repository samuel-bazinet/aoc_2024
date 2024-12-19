from functools import cache

@cache
def contains(to_check: str) -> int:
    ret_val = 0
    if len(to_check) == 0:
        return 1
    for t in available:
        if to_check.startswith(t):
            #print(':', to_check)
            #print(t)
            ret_val += contains(to_check[len(t):]) 
    return ret_val

with open('input.txt', 'r') as file:
    lines = file.readlines()

available = lines[0].strip().split(', ')

to_check = [line.strip() for line in lines[2:]]

result = 0

for t in to_check:
    r = contains(t)
    #print(r, '\n')
    result += r

print(result)