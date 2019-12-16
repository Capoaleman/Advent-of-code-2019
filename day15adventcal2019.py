from collections import defaultdict
import os
from time import sleep
import random


def clrscr():  # function to clear the console, something similar to clrscr() we know from C++
    if os.name == "posix":  # compatible with Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):  # compatible with DOS/Windows
        os.system('CLS')


def intercode_program(arr, i=0, rel_base=0, entry=0):
    # For animation purpose only
    # sleep(0.08)
    while i <= len(arr):
        # Add
        if arr[i] % 100 == 1:
            par1, par2, par3 = arr[i+1:i+4]
            mod_1par = arr[i] // 100 % 10
            mod_2par = arr[i] // 1000 % 10
            mod_3par = arr[i] // 10000 % 10
            x1 = par1 if mod_1par == 1 else arr[rel_base +
                                                par1] if mod_1par == 2 else arr[par1]
            x2 = par2 if mod_2par == 1 else arr[rel_base +
                                                par2] if mod_2par == 2 else arr[par2]
            x3 = rel_base + par3 if mod_3par == 2 else par3
            arr[x3] = x1+x2
            i += 4
        # Multiply
        elif arr[i] % 100 == 2:
            par1, par2, par3 = arr[i+1:i+4]
            mod_1par = arr[i] // 100 % 10
            mod_2par = arr[i] // 1000 % 10
            mod_3par = arr[i] // 10000 % 10
            x1 = par1 if mod_1par == 1 else arr[rel_base +
                                                par1] if mod_1par == 2 else arr[par1]
            x2 = par2 if mod_2par == 1 else arr[rel_base +
                                                par2] if mod_2par == 2 else arr[par2]
            x3 = rel_base + par3 if mod_3par == 2 else par3
            arr[x3] = x1*x2
            i += 4
        # get input
        elif arr[i] % 100 == 3:
            mod_1par = arr[i] // 100 % 10
            par1 = arr[i+1]
            resul = rel_base + par1 if mod_1par == 2 else par1
            arr[resul] = entry
            i += 2
        # set output
        elif arr[i] % 100 == 4:
            mod_1par = arr[i] // 100 % 10
            par1 = arr[i+1]
            resul = par1 if mod_1par == 1 else arr[rel_base +
                                                   par1] if mod_1par == 2 else arr[par1]
            i += 2
            return resul, True, i, rel_base

        # Jump-if-True
        elif arr[i] % 100 == 5:
            mod_1par = arr[i] // 100 % 10
            mod_2par = arr[i] // 1000 % 10
            par1, par2 = arr[i+1:i+3]
            x1 = par1 if mod_1par == 1 else arr[rel_base +
                                                par1] if mod_1par == 2 else arr[par1]
            x2 = par2 if mod_2par == 1 else arr[rel_base +
                                                par2] if mod_2par == 2 else arr[par2]
            i = x2 if x1 != 0 else i+3
        # Jump-if-False
        elif arr[i] % 100 == 6:
            mod_1par = arr[i] // 100 % 10
            mod_2par = arr[i] // 1000 % 10
            par1, par2 = arr[i+1:i+3]
            x1 = par1 if mod_1par == 1 else arr[rel_base +
                                                par1] if mod_1par == 2 else arr[par1]
            x2 = par2 if mod_2par == 1 else arr[rel_base +
                                                par2] if mod_2par == 2 else arr[par2]
            i = x2 if x1 == 0 else i+3
        # less than
        elif arr[i] % 100 == 7:
            par1, par2, par3 = arr[i+1:i+4]
            mod_1par = arr[i] // 100 % 10
            mod_2par = arr[i] // 1000 % 10
            mod_3par = arr[i] // 10000 % 10
            x1 = par1 if mod_1par == 1 else arr[rel_base +
                                                par1] if mod_1par == 2 else arr[par1]
            x2 = par2 if mod_2par == 1 else arr[rel_base +
                                                par2] if mod_2par == 2 else arr[par2]
            x3 = rel_base + par3 if mod_3par == 2 else par3
            arr[x3] = 1 if x1 < x2 else 0
            i += 4
        # equals
        elif arr[i] % 100 == 8:
            par1, par2, par3 = arr[i+1:i+4]
            mod_1par = arr[i] // 100 % 10
            mod_2par = arr[i] // 1000 % 10
            mod_3par = arr[i] // 10000 % 10
            x1 = par1 if mod_1par == 1 else arr[rel_base +
                                                par1] if mod_1par == 2 else arr[par1]
            x2 = par2 if mod_2par == 1 else arr[rel_base +
                                                par2] if mod_2par == 2 else arr[par2]
            x3 = rel_base + par3 if mod_3par == 2 else par3
            arr[x3] = 1 if x1 == x2 else 0
            i += 4
        # relative base
        elif arr[i] % 100 == 9:
            par1 = arr[i+1]
            mod_1par = arr[i] // 100 % 10
            x1 = par1 if mod_1par == 1 else arr[rel_base +
                                                par1] if mod_1par == 2 else arr[par1]
            rel_base = rel_base+x1
            i += 2
        elif arr[i] == 99:
            print("Halt 99 opcode")
            return "0", False, 0, rel_base
        else:
            raise ValueError("Unknown instruction {}".format(arr[i]))
    return


def get_paint(pan):
    """Paints the maze by following the robot"""
    clrscr()
    items = pan.items()
    min_x = min(items, key=lambda x: x[0][0])[0][0]
    min_y = min(items, key=lambda x: x[0][1])[0][1]
    max_x = max(items, key=lambda x: x[0][0])[0][0]
    max_y = max(items, key=lambda x: x[0][1])[0][1]
    for i in range(max_y+1, min_y-1, -1):
        for j in range(min_x-1, max_x+1):
            coor = (j, i)
            val = pan.get(coor, 0)
            if val == "#":
                print("#", end="")
            elif val == "R":
                print("R", end="")
            elif val == ".":
                print(".", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    f = open("./inputday15.txt", "r")
    input_arr = list(map(int, f.readline().split(",")))
    for i in range(500):
        input_arr.append(0)
    i = 0
    rel_base = 0
    flag = True
    x, y = 0, 0
    coord = (x, y)
    steps = 1
    mapa = defaultdict(int)
    mapa[coord] = "R"
    entry = 1
    pre_entry = 1
    max_steps = 0
    while flag:
        output, flag, i, rel_base = intercode_program(
            input_arr, i, rel_base, entry)
        if output == 0:  # direction of the robot 1 North, 2 south, 3 west, 4 east
            pre_entry = entry
            if entry == 1:
                new_coor = (x, y+1)
                entry = 4
            elif entry == 4:
                new_coor = (x+1, y)
                entry = 2
            elif entry == 2:
                new_coor = (x, y-1)
                entry = 3
            else:
                new_coor = (x-1, y)
                entry = 1
            mapa[new_coor] = "#"
        elif output == 1 or output == 2:
            coord = (x, y)
            if entry == 1:
                new_coor = (x, y+1)
                if pre_entry == 1:
                    pre_entry = 3
            elif entry == 2:
                new_coor = (x, y-1)
                if pre_entry == 2:
                    pre_entry = 4
            elif entry == 3:
                new_coor = (x-1, y)
                if pre_entry == 3:
                    pre_entry = 2
            else:
                if pre_entry == 4:
                    pre_entry = 1
                new_coor = (x+1, y)
            if output == 2:
                mapa[new_coor] = "O"
                # First part of the challenge
                print(f"The oxigen system is {steps} away")
                # Resets the steps and the map to begin with counting in the oxygen sys location
                max_steps = steps
                steps = 1
                for items in mapa.keys():
                    mapa[items] = " "
            if mapa[new_coor] == ".":
                mapa[new_coor] = "R"
                steps -= 1
                mapa[coord] = " "
            else:
                mapa[coord] = "."
                mapa[new_coor] = "R"
                steps += 1
            entry = pre_entry
            if steps > max_steps:
                max_steps = steps
            if max_steps > 6 and x == 0 and y == 0:
                break
            x, y = new_coor
        # ACTIVATE TO SEE THE ANIMATION
        # get_paint(mapa)
    # 2nd part of the challenge    
    print(f"Total of minutes to fill the map with oxigen: {max_steps}")
