# Advent of Code 2019
# challenge day 13
# https://adventofcode.com/2019/day/13
from collections import defaultdict


def intercode_program(arr, i=0, rel_base=0, entrada=0):
    """ Intercode program"""
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
            arr[resul] = entrada
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
            return 0, False, 0, rel_base
        else:
            raise ValueError("Unknown instruction {}".format(arr[i]))
    return


if __name__ == "__main__":
    f = open("./day 13/inputday13.txt", "r")
    input_arr = list(map(int, f.readline().split(",")))
    for i in range(500):
        input_arr.append(0)
    # Set the initial parameters
    flag = True
    i = 0
    rel_base = 0
    game_screen = defaultdict(int)
    joystick = 1
    ball = 0
    padle = 0
    # Game Loop
    while flag:
        x, flag, i, rel_base = intercode_program(
            input_arr, i, rel_base, joystick)
        if not flag:
            break
        y, flag, i, rel_base = intercode_program(
            input_arr, i, rel_base, joystick)
        if not flag:
            break
        tile_id, flag, i, rel_base = intercode_program(
            input_arr, i, rel_base, joystick)
        # get the position x of the ball and padle to simulate the joystick
        if tile_id == 4:
            ball = x
        if tile_id == 3:
            padle = x
        if ball == padle:
            joystick = 0
        elif ball > padle:
            joystick = 1
        else:
            joystick = -1
        if flag:
            if x == -1 and y == 0 and tile_id > 4:
                score = tile_id
                continue
            else:
                coor = (x, y)
                if game_screen[coor]:
                    if game_screen[coor] == 1:
                        continue
                    else:
                        game_screen[coor] = tile_id
                else:
                    game_screen[coor] = tile_id

    # 1st part of the challenge, counts the total blocks.
    count = 0
    for i in game_screen.values():
        if i == 2:
            count += 1
    print(count)
    # 2nd answer of the challenge after changing
    print(score)
