# Advent of Code 2019
# challenge day 11
# https://adventofcode.com/2019/day/11
from collections import defaultdict
from copy import deepcopy


def intercode_program(arr, i=0, rel_base=0, entrada=0):
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
            return "0", False, 0, rel_base
        else:
            raise ValueError("Unknown instruction {}".format(arr[i]))
    return


class Robot:
    def __init__(self, code):
        self.code = code
        self.direction = "UP"
        self.position = (0, 0)
        self.painted = defaultdict(int)
        self.path = defaultdict(int)

    def get_paint(self):
        """Paint the code in the spacecraft"""
        items = self.painted.items()
        min_x = min(items, key=lambda x: x[0][0])[0][0]
        min_y = min(items, key=lambda x: x[0][1])[0][1]
        max_x = max(items, key=lambda x: x[0][0])[0][0]
        max_y = max(items, key=lambda x: x[0][1])[0][1]
        for y in range(max_y, min_y-1, -1):
            for x in range(min_x, max_x):
                pos = (x, y)
                if self.painted[pos]:
                    if self.painted[pos] == 1:
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    print(" ", end="")
            print()

    def get_move(self, turn):
        """Set the new position of the robot and change its direction"""
        x, y = self.position
        if turn == 0:
            if self.direction == "UP":
                self.direction = "LF"
                new_pos = (x-1, y)
            elif self.direction == "LF":
                self.direction = "DW"
                new_pos = (x, y-1)
            elif self.direction == "DW":
                self.direction = "RG"
                new_pos = (x+1, y)
            else:
                self.direction = "UP"
                new_pos = (x, y+1)
        elif turn == 1:
            if self.direction == "UP":
                self.direction = "RG"
                new_pos = (x+1, y)
            elif self.direction == "RG":
                self.direction = "DW"
                new_pos = (x, y-1)
            elif self.direction == "DW":
                self.direction = "LF"
                new_pos = (x-1, y)
            else:
                self.direction = "UP"
                new_pos = (x, y+1)
        self.path[new_pos] = 1
        self.position = new_pos
        return self

    def run(self):
        """Turn on the robot and let the magic happen"""
        self.path[(0, 0)] = 1
        flag = True
        pointer = 0
        rel_base = 0
        # inpu = 0 for part 1, 1 for part 2 of the challenge
        inpu = 1
        while flag:
            if self.painted[self.position]:
                color, flag, pointer, rel_base = intercode_program(
                    self.code, pointer, rel_base, self.painted[self.position])
            else:
                color, flag, pointer, rel_base = intercode_program(
                    self.code, pointer, rel_base, inpu)
                inpu = 0
            if flag:
                self.painted[self.position] = color
                change, flag, pointer, rel_base = intercode_program(
                    self.code, pointer, rel_base)
                if flag:
                    self.get_move(change)
        print(len(self.painted))
        self.get_paint()


if __name__ == "__main__":
    f = open("./day 11/inputday11.txt", "r")
    input_arr = list(map(int, f.readline().split(",")))
    for i in range(500):
        input_arr.append(0)
    paint_robot = Robot(input_arr)
    paint_robot.run()
