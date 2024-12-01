
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

for (l, r) in zip(list_a, list_b):
    out += abs(l - r)

print(out)