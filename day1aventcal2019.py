# Function for the 1st part os the challenge
def comb_cal(mass):
    return mass//3-2

# Function for the 2nd part of the challenge
def comb_cal(mass):
    res = mass//3-2
    if res <= 0:
        return 0
    else:
        return res + comb_cal(res)

# Main stays the same for both parts
if __name__ == "__main__":
    total_fuel = 0
    f = open("./inputday1.txt", "r")
    filename = f.readlines()
    for line in filename:
        total_fuel += comb_cal(int(line))
    print(total_fuel)
