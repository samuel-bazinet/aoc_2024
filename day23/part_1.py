

with open('input.txt', 'r') as file:
    lines = file.readlines()
neighs: dict[str, list[str]] = {}

for line in lines:
    line = line.strip().split('-')
    l = line[0]
    r = line[1]
    if l not in neighs.keys():
        neighs[l] = [r]
    else:
        neighs[l].append(r)
    if r not in neighs.keys():
        neighs[r] = [l]
    else:
        neighs[r].append(l)

trips: list[set[str]] = []

for k, v in neighs.items():
    for n in v:
        for n2 in neighs[n]:
            if n2 in v:
                if {k, n, n2} not in trips:
                    trips.append({k,n,n2})
print(len(trips))

trimmed = []

for trip in trips:
    g = False
    for c in trip:
        if c[0] == 't':
            g = True

    if g:
        trimmed.append(trip)

print(len(trimmed))