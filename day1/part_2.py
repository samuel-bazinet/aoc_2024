
with open('input.txt', 'r') as file:
    lines = file.readlines()

pairs = [a.strip().split('   ') for a in lines]
print(pairs)
list_a = []
list_b = []
for e in pairs:
    list_a.append(int(e[0]))
    list_b.append(int(e[1]))

list_a.sort()
list_b.sort()
print(list_a)
print(list_b)

out = 0

for i in list_a:
    count = 0
    for j in list_b:
        if i == j:
            count += 1
    out += count*i

print(out)