# Advent of Code 2019
# challenge day 10
# https://adventofcode.com/2019/day/10
from collections import namedtuple as ndt
from copy import deepcopy
from math import atan, pi


def coordenates(mapa):
    """ Returns the coordenates for all the asteroids in the map"""
    ast_coor = ndt("ast_coor", "x y")
    coor_map = []
    for r in range(y_len):
        for c in range(x_len):
            if mapa[r][c] == "#":
                coor_map.append(ast_coor(x=c, y=r))
    return coor_map


def straight_line(p1, p2):
    """Returns the equation of the straight of the 2 points, the angletion and angle"""
    par1 = (p2.y-p1.y)
    par2 = (p2.x-p1.x)
    try:
        angle = atan(par1/par2)
        if par2 > 0:
            direc = 1
        else:
            direc = -1
    except ZeroDivisionError:
        if par1 < 0:
            angle = -pi/2
            direc = -1
        else:
            angle = pi/2
            direc = 1
    return [par1, par1*p1.x, par2, par2*p1.y, angle, direc, p2]


def num_aster(mon_sta, ste_map):
    """Find the best location for a new monitoring station, return the number of asteroids detected and 
        station coordenates"""
    sight = []
    num_as = 0
    for ast in ste_map:
        flag = True
        for line in sight:
            if (line[0]*ast.x-line[1]-line[2]*ast.y+line[3]) == 0:
                try:
                    angle = atan((ast.y-mon_sta.y)/(ast.x-mon_sta.x))
                    if (ast.x-mon_sta.x) > 0:
                        direc = 1
                    else:
                        direc = -1
                except ZeroDivisionError:
                    if (ast.y-mon_sta.y) < 0:
                        angle = -pi/2
                        direc = -1
                    else:
                        angle = pi/2
                        direc = 1
                if angle == line[4] and direc == line[5]:
                    flag = False
                    break
        if flag:
            num_as += 1
            sight.append(straight_line(mon_sta, ast))
    # 2nd part of the challenge, you know now here where to put the monitor station
    # prints the 200th asteroid to be vaporized with x * 100 + y of its coordenates
    if mon_sta == (22, 25):
        for i in sight:
            if i[5] == 1:
                i[4] += pi/2
            else:
                i[4] += 3*pi/2
                if i[4] == pi:
                    i[4] = 0
                    i[5] = 1
        new_sight = sorted(sight, key=lambda x: x[4])
        print(new_sight[199][6].x*100+new_sight[199][6].y)
    return num_as


if __name__ == "__main__":
    f = open("./day 10/inputday10.txt", "r")
    input_map = []
    fil = f.readlines()
    for line in fil:
        inp_lines = line.split("\n")
        input_map.append(inp_lines[0])
    x_len = len(input_map[0])
    y_len = len(input_map)
    coor_map = coordenates(input_map)
    max_ast = []
    for item in coor_map:
        new_map = deepcopy(coor_map)
        new_map.remove(item)
        max_ast.append((num_aster(item, new_map), item))
        del new_map
    # 1st part of the challenge
    print(max(max_ast)[0])
