# Advent of Code 2019
# challenge day 14
# https://adventofcode.com/2019/day/14
from collections import defaultdict
import math


def get_ore(react, sol, amount=1):
    """return the amount of ore to produce a specific amount of Fuel"""
    requeriments = {"FUEL": amount}
    while True:
        try:
            need, need_amount = next(
                (n, i) for n, i in requeriments.items() if n != "ORE" and i > 0)
        except:
            break
        size = sol[need]
        add_items = react[need]
        mult_reac = math.ceil(need_amount/size)
        for chem, val in add_items.items():
            requeriments[chem] = requeriments.get(
                chem, 0) + mult_reac * val
        requeriments[need] -= mult_reac*size
    return requeriments["ORE"]


def get_max_fuel(reactives, sol, max_cargo, ore_for_one):
    """Get the max fuel that the Inter-Stellar Refinery can produce
        with a given amount of ore, uses binary search"""
    lo_fuel = max_cargo//ore_for_one
    hi_fuel = lo_fuel*2
    while True:
        fuel = (hi_fuel+lo_fuel)//2
        ore = get_ore(reactives, sol_size, fuel)
        if ore > max_cargo:
            hi_fuel = fuel
        elif ore < max_cargo:
            lo_fuel = fuel
        if (max_cargo-ore_for_one) < ore <= max_cargo:
            break
    return fuel


if __name__ == "__main__":
    f = open("./day 14/inputday14.txt", "r")
    sol_size = defaultdict(int)
    reactives = defaultdict(dict)
    for line in f.readlines():
        chemicals, result = line.strip("\n").split(" => ")
        amount, name = result.split(" ")
        sol_size[name] = int(amount)
        for item in chemicals.split(", "):
            amount, reac_name = item.split(" ")
            reactives[name][reac_name] = int(amount)
    # 1st part of the challenge
    ore_for_one = get_ore(reactives, sol_size)
    print(f"Total ore required {ore_for_one}")

    # 2nd part of the challenge (binary search)
    max_cargo = 10**12
    fuel = get_max_fuel(reactives, sol_size, max_cargo, ore_for_one)
    print(f"Max fuel production with 1 trillon ore: {fuel}")
