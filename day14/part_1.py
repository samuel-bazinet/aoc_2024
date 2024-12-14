
from dataclasses import dataclass

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
    for _ in range(seconds):
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

with open('input.txt', 'r') as file:
    lines = file.readlines()

out = [0, 0, 0, 0]

robots: list[Robot] = []

for line in lines:
    robots.append(parse_robot(line))

for robot in robots:
    move_robot(robot)
    q = r_i_q(robot)
    if q >= 0:
        out[q]+= 1

print(out[0]*out[1]*out[2]*out[3])
