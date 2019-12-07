# Advent of Code 2019
# challenge day 7
# https://adventofcode.com/2019/day/7

from itertools import permutations


def grav_asis_prog(arr, entrada, output, i=0):
    flag = True
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
            if flag:
                arr[par1] = entrada
                flag = False
            else:
                arr[par1] = output
            i += 2
        # set output
        elif arr[i] % 100 == 4:
            par1 = arr[i+1]
            resul = par1 if (arr[i] // 100 % 10) == 1 else arr[par1]
            i += 2
            # return for the 1st part of the challenge
            return resul, True, i
            # print(resul)

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
            return output, False, 0
        else:
            raise ValueError("Unknown instruction {}".format(arr[i]))
    return resul, True


if __name__ == "__main__":
    f = open("./aventcal2019/day 7/inputday7.txt", "r")
    input_arr = list(map(int, f.readline().split(",")))
    # part 2 of the challenge
    arr_out = []
    for item in permutations([5, 6, 7, 8, 9], 5):
        output = 0
        arr_A = input_arr.copy()
        arr_B = input_arr.copy()
        arr_C = input_arr.copy()
        arr_D = input_arr.copy()
        arr_E = input_arr.copy()
        output, flag, i_a = grav_asis_prog(arr_A, item[0], output)
        output, flag, i_b = grav_asis_prog(arr_B, item[1], output)
        output, flag, i_c = grav_asis_prog(arr_C, item[2], output)
        output, flag, i_d = grav_asis_prog(arr_D, item[3], output)
        output, flag, i_e = grav_asis_prog(arr_E, item[4], output)
        while flag:
            output, flag, i_a = grav_asis_prog(arr_A, output, output, i_a)
            output, flag, i_b = grav_asis_prog(arr_B, output, output, i_b)
            output, flag, i_c = grav_asis_prog(arr_C, output, output, i_c)
            output, flag, i_d = grav_asis_prog(arr_D, output, output, i_d)
            output, flag, i_e = grav_asis_prog(arr_E, output, output, i_e)
            if not flag:
                arr_out.append(output)
    print(max(arr_out))
    # Part 1 of the challenge
    total_output = []
    for item in permutations([0, 1, 2, 3, 4], 5):
        output = 0
        for phase in item:
            output = grav_asis_prog(input_arr, phase, output)
            total_output.append(output)
    print(max(total_output))
