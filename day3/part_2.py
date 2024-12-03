import re 
from functools import reduce

with open('input.txt', 'r') as file:
    file_content = file.read()

matches = re.finditer("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", file_content)

result = 0
on = True

for mul in matches:
    if mul.group() == 'do()':
        print(mul)
        on = True
    elif mul.group() == "don't()":
        print(mul)
        on = False
    elif on:
        content = mul.group()[4:-1]
        result += reduce(lambda x, y: x*y, (int(i) for i in content.split(',')))

print(result)