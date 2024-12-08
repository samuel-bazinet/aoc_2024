from itertools import combinations

with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [[char for char in line.strip()] for line in lines]

antennas: dict[str, list[tuple[int, int]]] = dict()
found: set[tuple[int, int]] = set()

h = len(lines) - 1
w = len(lines[0]) - 1

for i, row in enumerate(lines):
    for j, char in enumerate(row):
        if char != '.':
            if char in antennas:
                antennas[char].append((i, j))
            else:
                antennas[char] = [(i, j)]

for points in antennas.values():
    pairs = combinations(points, 2)
    for pair in pairs:
        y_diff = pair[0][0] - pair[1][0]
        x_diff = pair[0][1] - pair[1][1]
        if 0 <= (y := pair[0][0] - y_diff) <= h and 0 <= (x:= pair[0][1] - x_diff) <= w:
            if (y, x) != pair[1]:
                found.add((y, x))
        if 0 <= (y := pair[0][0] + y_diff) <= h and 0 <= (x:= pair[0][1] + x_diff) <= w:
            if (y, x) != pair[1]:
                found.add((y, x))
        if 0 <= (y := pair[1][0] - y_diff) <= h and 0 <= (x:= pair[1][1] - x_diff) <= w:
            if (y, x) != pair[0]:
                found.add((y, x))
        if 0 <= (y := pair[1][0] + y_diff) <= h and 0 <= (x:= pair[1][1] + x_diff) <= w:
            if (y, x) != pair[0]:
                found.add((y, x))

for p in found:
    lines[p[0]][p[1]] = '#'

for r in lines:
    for c in r:
        print(c, end='')
    print()

print(len(found))
