from copy import deepcopy


def intercode_program(arr, i=0, rel_base=0, entry=0):
    resul = 0
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
            arr[resul] = int(input("Enter data:"))
            i += 2
        # set output
        elif arr[i] % 100 == 4:
            mod_1par = arr[i] // 100 % 10
            par1 = arr[i+1]
            resul = par1 if mod_1par == 1 else arr[rel_base +
                                                   par1] if mod_1par == 2 else arr[par1]
            i += 2
            print(chr(resul), end="")
            # FOR THE 2ND PART OF THE CHALLENGE TO WORK, NEED TO DISABLE
            # THE RETURN FOR THE OPCODE 4 AND RUN THE PROGRAM
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
            return resul, False, 0, rel_base
        else:
            raise ValueError("Unknown instruction {}".format(arr[i]))
    return

def get_map(code):
    """Generates the map of the outside of the ship"""
    i = 0
    rel_base = 0
    flag = True
    x, y = 0, 0
    mapa = {}
    while flag:
        coord = (x, y)
        output, flag, i, rel_base = intercode_program(
            input_arr, i, rel_base)
        if not flag:
            break
        if output == 10:
            y -= 1
            x = 0
            continue
        else:
            if mapa.get((x-1, y), 0) == "#" and mapa.get((x, y+1), 0) == "#" and output == 35:
                mapa[coord] = "O"
            else:
                mapa[coord] = chr(output)
            x += 1
    return mapa


def camara_calibration(mapa):
    """ Calibrates the camara with the sum of the alignment parameters
    a aligment parameter is: the result of the number of space units from the top multiplied 
    by the number of space units from the left of the map"""
    intersections = []
    for key, val in mapa.items():
        if val == "O":
            if mapa.get((key[0]-1, key[1]), 0) == "#" and mapa.get((key[0]+1, key[1]), 0) == "#" and mapa.get((key[0], key[1]-1), 0) == "#" and mapa.get((key[0], key[1]+1), 0) == "#":
                intersections.append(key[0]*abs(key[1]))
            else:
                mapa[(key[0], key[1])] = "#"
    print(f"the sum of the alignment is {sum(intersections)}")
    return mapa



if __name__ == "__main__":
    f = open("./day 17/inputday17.txt", "r")
    input_arr = list(map(int, f.readline().split(",")))
    for i in range(5000):
        input_arr.append(0)
    part2_arr = deepcopy(input_arr)
    # Part 1 of the challenge
    mapa = get_map(input_arr)
    mapa = camara_calibration(mapa)

    #Part 2 of the challenge, override the movements of the robot
    # FOR THE 2ND PART OF THE CHALLENGE TO WORK, NEED TO DISABLE
    # THE RETURN LINE FOR THE OPCODE 4 AND RUN THE PROGRAM
    part2_arr[0] = 2
    # movement routine = A,B,A,B,C,C,B,C,B,A
    mov_routine = [65,44,66,44,65,44,66,44,67,44,67,44,66,44,67,44,66,44,65,10]
    # Function A: R,8,4,L,8,R,8,4
    func_A = [82,44,56,44,52,44,76,44,56,44,82,44,56,44,52,10]
    # Function B: R,8,R,6,R,6,R,8
    func_B = [82,44,56,44,82,44,54,44,82,44,54,44,82,44,56,10]
    # Function C: R,8,L,8,R,8,R,4,R,4
    func_C = [82,44,56,44,76,44,56,44,82,44,56,44,82,44,52,44,82,44,52,10]
    # Video feet = n
    video = [110,10]
    # Enter the data manually
    #----------------- enable fot the 2nd part-----------------
    #output = intercode_program(part2_arr)
    #print(f"Dust collected: {output[0]}")