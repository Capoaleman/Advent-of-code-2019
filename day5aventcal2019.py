# Advent of Code 2019
# challenge day 5
# https://adventofcode.com/2019/day/5


def grav_asis_prog(arr):
    i = 0
    while i <= len(arr):
        # Add
        if arr[i] % 100 == 1:
            par1, par2, par3 = arr[i+1:i+4]
            mod_1par = arr[i] // 100 % 10
            mod_2par = arr[i] // 1000 % 10
            x1 = par1 if mod_1par == 1 else arr[par1]
            x2 = par2 if mod_2par == 1 else arr[par2]
            arr[par3] = x1+x2
            i += 4
        # Multiply
        elif arr[i] % 100 == 2:
            par1, par2, par3 = arr[i+1:i+4]
            mod_1par = arr[i] // 100 % 10
            mod_2par = arr[i] // 1000 % 10
            x1 = par1 if mod_1par == 1 else arr[par1]
            x2 = par2 if mod_2par == 1 else arr[par2]
            arr[par3] = x1*x2
            i += 4
        # get input
        elif arr[i] % 100 == 3:
            par1 = arr[i+1]
            arr[par1] = int(input("opcode 3, waiting  for input: "))
            i += 2
        # set output
        elif arr[i] % 100 == 4:
            par1 = arr[i+1]
            resul = par1 if (arr[i] // 100 % 10) == 1 else arr[par1]
            print(resul)
            i += 2
        # -------------------------------
        # Extra 2nd part of the challenge
        # --------------------------------
        # Jump-if-True
        elif arr[i] % 100 == 5:
            mod_1par = arr[i] // 100 % 10
            mod_2par = arr[i] // 1000 % 10
            par1, par2 = arr[i+1:i+3]
            x1 = par1 if mod_1par == 1 else arr[par1]
            x2 = par2 if mod_2par == 1 else arr[par2]
            i = x2 if x1 != 0 else i+3
        # Jump-if-False
        elif arr[i] % 100 == 6:
            mod_1par = arr[i] // 100 % 10
            mod_2par = arr[i] // 1000 % 10
            par1, par2 = arr[i+1:i+3]
            x1 = par1 if mod_1par == 1 else arr[par1]
            x2 = par2 if mod_2par == 1 else arr[par2]
            i = x2 if x1 == 0 else i+3
        # less than
        elif arr[i] % 100 == 7:
            par1, par2, pos = arr[i+1:i+4]
            mod_1par = arr[i] // 100 % 10
            mod_2par = arr[i] // 1000 % 10
            x1 = par1 if mod_1par == 1 else arr[par1]
            x2 = par2 if mod_2par == 1 else arr[par2]
            arr[pos] = 1 if x1 < x2 else 0
            i += 4
        # equals
        elif arr[i] % 100 == 8:
            par1, par2, pos = arr[i+1:i+4]
            mod_1par = arr[i] // 100 % 10
            mod_2par = arr[i] // 1000 % 10
            x1 = par1 if mod_1par == 1 else arr[par1]
            x2 = par2 if mod_2par == 1 else arr[par2]
            arr[pos] = 1 if x1 == x2 else 0
            i += 4
        elif arr[i] == 99:
            break
        else:
            raise ValueError("Unknown instruction {}".format(arr[i]))
    return


if __name__ == "__main__":
    f = open("./aventcal2019/day 5/inputday5.txt", "r")
    input_arr = list(map(int, f.readline().split(",")))
    grav_asis_prog(input_arr)
