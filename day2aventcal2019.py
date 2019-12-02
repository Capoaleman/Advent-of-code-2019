# Solution of the 1st part of the challenge
def grav_asis_prog(input_arr):
    length = len(input_arr)
    for i in range(0, length, 4):
        ind_res = input_arr[i+3]
        ind_1 = input_arr[i+1]
        ind_2 = input_arr[i+2]
        if input_arr[i] == 1:
            result = input_arr[ind_1]+input_arr[ind_2]
            input_arr[ind_res] = result
        elif input_arr[i] == 2:
            result = input_arr[ind_1]*input_arr[ind_2]
            input_arr[ind_res] = result
        elif input_arr[i] == 99:
            break
    return input_arr


# Solution of the 2nd part of the challenge
OUTPUT = 19690720


def noun_verb_find(arr):
    for verb in range(100):
        for noun in range(100):
            new_arr = arr.copy()
            new_arr[1] = noun
            new_arr[2] = verb
            new_arr = grav_asis_prog(new_arr)
            if new_arr[0] == OUTPUT:
                print(new_arr)
                return noun, verb
            elif new_arr[0] > OUTPUT:
                del new_arr
                break
            else:
                del new_arr
                continue


if __name__ == "__main__":
    f = open("./aventcal2019/day 2/inputday2.txt", "r")
    input_arr = list(map(int, f.readline().split(",")))

    # 1st part result
    result = grav_asis_prog(input_arr)
    print(result[0])

    # 2nd part result
    noun, verb = noun_verb_find(input_arr)
    print(100*noun+verb)
