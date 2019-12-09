# Advent of Code 2019
# challenge day 9
# https://adventofcode.com/2019/day/9


def grav_asis_prog(arr):
    i = 0
    rel_base = 0
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
            arr[resul] = int(input("opcode 3, waiting  for input: "))
            i += 2
        # set output
        elif arr[i] % 100 == 4:
            mod_1par = arr[i] // 100 % 10
            par1 = arr[i+1]
            output = par1 if mod_1par == 1 else arr[rel_base +
                                                    par1] if mod_1par == 2 else arr[par1]
            print(output)
            i += 2
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
            break
        else:
            raise ValueError("Unknown instruction {}".format(arr[i]))
    return


if __name__ == "__main__":
    f = open("./day 9/inputday9.txt", "r")
    input_arr = list(map(int, f.readline().split(",")))
    for i in range(500):
        input_arr.append(0)
    grav_asis_prog(input_arr)
