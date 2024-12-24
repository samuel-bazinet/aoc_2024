

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
    current_trip = {k}
    for n in v:
        to_add = True
        for n2 in current_trip:
            if n2 not in neighs[n]:
                to_add = False
                break
        if to_add:
            current_trip.add(n)
    if current_trip not in trips:
        trips.append(current_trip)
        
lengths: list[int] = [len(t) for t in trips]
l_i = lengths.index(max(lengths))
l_t = list(trips[l_i])

print(','.join(sorted(l_t)))