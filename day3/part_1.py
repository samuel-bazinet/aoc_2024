import re 
from functools import reduce

with open('input.txt', 'r') as file:
    file_content = file.read()

matches = re.findall('mul\(\d{1,3},\d{1,3}\)', file_content)

result = 0

for mul in matches:
    content = mul[4:-1]
    result += reduce(lambda x, y: x*y, (int(i) for i in content.split(',')))

print(result)