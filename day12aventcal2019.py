# Advent of Code 2019
# challenge day 12
# https://adventofcode.com/2019/day/12
from copy import deepcopy
from math import gcd


def new_velocity(pos, vel):
    """Calculates the new velocity of the moon"""
    for j, moon in enumerate(pos):
        for pair_moon in pos:
            for i in range(3):
                if moon[i] > pair_moon[i]:
                    vel[j][i] -= 1
                elif moon[i] < pair_moon[i]:
                    vel[j][i] += 1
    return vel


def new_position(pos, vel):
    """Calculates the new position od the moons"""
    for i in range(4):
        for j in range(3):
            pos[i][j] += vel[i][j]

    return pos


def get_energy(pos, vel):
    """Calculates the total energy in the system"""
    total = 0
    for i in range(4):
        pot, kin = 0, 0
        for j in range(3):
            pot += abs(pos[i][j])
            kin += abs(vel[i][j])
        total += pot*kin
    return total


def lcm(a, b, c):
    """Calculates the least common multiple for 3 integers"""
    gcd2 = gcd(a, b)
    lcm2 = a*b // gcd2
    lcm3 = c*lcm2 // gcd(c, lcm2)
    return lcm3


if __name__ == "__main__":
    f = open("./day 12/inputday12.txt", "r")
    position = []
    velocity = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    fil = f.readlines()
    for line in fil:
        pos = line.strip("<=>x\n").split(",")
        for i in range(3):
            pos[i] = int(pos[i].strip(" y=z"))
        position.append(pos)
    inc_pos = deepcopy(position)
    inc_vel = deepcopy(velocity)
    # 1st part of the challenge
    for step in range(1000):
        velocity = new_velocity(position, velocity)
        position = new_position(position, velocity)
    print(get_energy(position, velocity))

    ax = []
    """ For every axis (x,y,z) calculates the cycle for it to return
    to the initial state, and then the lcm of the 3 is the answer"""
    for i in range(3):
        count = 1
        axis = 0
        position = deepcopy(inc_pos)
        velocity = deepcopy(inc_vel)
        while True:
            velocity = new_velocity(position, velocity)
            position = new_position(position, velocity)
            count += 1
            for j in range(4):
                if position[j][i] == inc_pos[j][i]:
                    axix += 1
                else:
                    axix = 0
                    break
            if axix == 4:
                break
        ax.append(count)
    # 2nd part result
    print(lcm(ax[0], ax[1], ax[2]))
