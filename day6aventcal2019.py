# Advent of Code 2019
# challenge day 6
# https://adventofcode.com/2019/day/5


# 1st part challenge
def sum_orbit_obj(start, center, orbit, total, path):
    """ Returns the total number of direct and indirect 
        orbits from the data map"""
    while True:
        path += 1
        count = center.count(start)
        if count == 1:
            ind = center.index(start)
            start = orbit[ind]
            total += path
        elif count > 1:
            total += path
            for i in range(length):
                if center[i] == start:
                    next_star = orbit[i]
                    total = sum_orbit_obj(next_star,
                                          center, orbit, total, path)
            return total
        elif count == 0:
            total += path
            return total

# 2nd parth challenge


def mov_spaces(obj, center, orbit):
    """ Returns the path from and object to the
        COM, via orbital transfer"""
    path = []
    while obj != "COM":
        ind = orbit.index(obj)
        obj = center[ind]
        path.append(obj)
    return path


if __name__ == "__main__":
    f = open("./aventcal2019/day 6/inputday6.txt", "r")
    center_obj = []
    orbit_obj = []
    input_arr = f.readlines()
    for line in input_arr:
        center_obj.append(line[:3])
        orbit_obj.append(line[4:7])
    length = len(center_obj)
    print(sum_orbit_obj("COM", center_obj, orbit_obj, 0, -1))

    # Transforms both paths into sets, the total of different items
    # in boths sets is the total step between them
    you_path = set(mov_spaces("YOU", center_obj, orbit_obj))
    san_path = set(mov_spaces("SAN", center_obj, orbit_obj))
    path_to_santa = you_path.symmetric_difference(san_path)
    print(len(path_to_santa))
