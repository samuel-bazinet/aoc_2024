
from dataclasses import dataclass
from time import sleep

@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int

#REAL
W = 101
H = 103
#TEST
#W = 11
#H = 7

seconds = 100

def parse_robot(line: str) -> Robot:
    line = line.strip().split(' ')
    p = line[0][2:].split(',')
    v = line[1][2:].split(',')
    return Robot(int(p[0]), int(p[1]), int(v[0]), int(v[1]))

def move_robot(robot: Robot) -> Robot:
    robot.px += robot.vx
    if robot.px < 0:
        robot.px += W
    elif robot.px > W-1:
        robot.px -= W
    robot.py += robot.vy
    if robot.py < 0:
        robot.py += H
    elif robot.py > H-1:
        robot.py -= H
    return robot

def r_i_q(r: Robot) -> int:
    hW = W//2
    hH = H//2
    if r.px < hW:
        if r.py < hH:
            return 0
        elif r.py > hH:
            return 1
    elif r.px > hW:
        if r.py < hH:
            return 2
        elif r.py > hH:
            return 3
    return -1

def line_exist(grid) -> bool:
    for i in range(H):
        counter = 0
        for j in range(W):
            if grid[i][j] == '*':
                counter += 1
            else:
                counter = 0
            if counter > 5:
                return True
    return False


with open('input.txt', 'r') as file:
    lines = file.readlines()

robots: list[Robot] = []

for line in lines:
    robots.append(parse_robot(line))

for i in range(15000):
    out = [[" " for _ in range(W)] for _ in range(H)]
    l = 0
    r = 0
    for robot in robots:
        move_robot(robot)

        out[robot.py][robot.px] = "*"
    if line_exist(out):
        # It'll show up eventually :)
        print("Second: ", i)
        for r in out:
            for e in r:
                print(e, end='')
            print()
        print()
        sleep(0.1)
    