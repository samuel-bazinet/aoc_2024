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
        o_y = y_diff = pair[0][0] - pair[1][0]
        o_x = x_diff = pair[0][1] - pair[1][1]
        counter = 1
        running = True
        while running:
            to_c = 0
            if 0 <= (y := pair[0][0] - y_diff) <= h and 0 <= (x:= pair[0][1] - x_diff) <= w:
                found.add((y, x))
            else:
                to_c += 1
            if 0 <= (y := pair[0][0] + y_diff) <= h and 0 <= (x:= pair[0][1] + x_diff) <= w:
                found.add((y, x))
            else:
                to_c += 1
            if 0 <= (y := pair[1][0] - y_diff) <= h and 0 <= (x:= pair[1][1] - x_diff) <= w:
                found.add((y, x))
            else:
                to_c += 1
            if 0 <= (y := pair[1][0] + y_diff) <= h and 0 <= (x:= pair[1][1] + x_diff) <= w:
                found.add((y, x))
            else:
                to_c += 1
            if to_c == 4:
                running = False
            counter += 1
            x_diff = o_x * counter
            y_diff = o_y * counter
            

for p in found:
    if lines[p[0]][p[1]] == '.':
        lines[p[0]][p[1]] = '#'

for r in lines:
    for c in r:
        print(c, end='')
    print()

print(len(found))
