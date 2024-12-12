
with open('input.txt', 'r') as file:
    lines = file.readlines()
grid = [[char for char in line.strip()] for line in lines]

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
H = len(grid)
W = len(grid[0])

visited: set[tuple[int, int]] = set()

def find_region(grid: list[list[str]], curr: str, loc: tuple[int, int]) -> tuple[int, int, list[tuple[int,int]]]:
    out = [1, 0]
    region = [loc]
    visited.add(loc)
    for dir in DIRS:
        y = loc[0]+dir[0]
        x = loc[1]+dir[1]
        if H <= y or y < 0 or W <= x or x < 0:
            out[1]+= 1
        else:
            if grid[y][x] == curr and (y, x) not in visited:
                r= find_region(grid, curr, (y, x))
                out[0] += r[0]
                out[1] += r[1]
                region.extend(r[2])
            elif grid[y][x] != curr:
                out[1] += 1
    return (out[0], out[1], region)

def get_sides(region: set[tuple[int, int]]) -> int:
    # go through each row, and if encounter a loc in region and last ins't in region and at most 1 of top and bottom is also in region, add side
    # repeat for columns
    # it is a square so can do both side at same time :)
    out = 0
    for y in range(-1, H+1):
        in_xt = False
        in_xb = False
        in_yl = False
        in_yr = False

        for x in range(-1, H+1):
            if (y, x) in region:
                in_xt = False
                in_xb = False
            if (x, y) in region:
                in_yl = False
                in_yr = False
                
            if (y+1, x) in region: 
                n = not (y, x) in region
                if not in_xt and n:
                    #print(y, x, "x from top in")
                    in_xt = True
                    out += 1
            else:
                in_xt = False
                

            if (y-1, x) in region: 
                n = not (y, x) in region
                if not in_xb and n:
                    #print(y, x, "x from bottom in")
                    in_xb = True
                    out += 1
            else:
                in_xb = False
                

            if (x, y+1) in region: 
                n = not (x, y) in region
                if not in_yl and n:
                    #print(x, y, "y from left in")
                    in_yl = True
                    out += 1
            else:
                in_yl = False
                

            if (x, y-1) in region: 
                n = not (x, y) in region
                if not in_yr and n:
                    #print(x, y, "y from right in")
                    in_yr = True
                    out += 1
            else:
                in_yr = False
                

    return out


result = 0

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if (y, x) not in visited:
            (a, p, s) = find_region(grid, char, (y, x))
            sides = get_sides(set(s))
            #print(char, a, sides)
            result += a*sides

print(result)