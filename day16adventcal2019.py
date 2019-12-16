from copy import deepcopy

P1 = [0]
P2 = [1]
P3 = [0]
P4 = [-1]


if __name__ == "__main__":
    f = open("./day 16/inputday16.txt", "r")
    input_arr = list(map(int, f.readline()))
    input_part2 = deepcopy(input_arr)
    length = len(input_arr)
    offset = int("".join(map(str, deepcopy(input_arr[:7]))))
    pattern_array = []
    for i in range(1, length+1):
        actual_pattern = (P1*i+P2*i+P3*i+P4*i)*(length//4+5)
        pattern_array.append(actual_pattern[1:length+1])
    new_arr = [""]*length
    for _ in range(100):
        for h, pattern in enumerate(pattern_array):
            new_arr[h] = abs(
                sum(list(map(lambda x, y: x*y, pattern, input_arr)))) % 10
        input_arr = new_arr
    print("".join(map(str, input_arr[0:8])))

    # 2nd part of the challenge
    input_part2 = (input_part2*10000)[offset:]
    length = len(input_part2)
    for _ in range(100):
        suma = 0
        for j in range(length-1, -1, -1):
            input_part2[j] = suma = (input_part2[j] + suma) % 10
    print("".join(map(str, input_part2[:8])))
