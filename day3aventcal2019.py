# This can be improved, but it was my first approach ;)
# Solution day 3!!!


def wire_path(wire):
    path1 = [(0, 0)]
    for i, path in enumerate(wire):
        if path[:1] == "R":
            x, y = path1[i][0] + int(path[1:]), path1[i][1]
            path1.append((x, y))
        elif path[:1] == "L":
            x, y = path1[i][0] - int(path[1:]), path1[i][1]
            path1.append((x, y))
        elif path[:1] == "U":
            x, y = path1[i][0], path1[i][1] + int(path[1:])
            path1.append((x, y))
        elif path[:1] == "D":
            x, y = path1[i][0], path1[i][1] - int(path[1:])
            path1.append((x, y))
    return path1


def get_intersections(path1, wire2):
    intersections = []
    start = (0, 0)
    for j, path in enumerate(wire2):
        if path[:1] == "R":
            x, y = start[0] + int(path[1:]), start[1]
            for j, point1 in enumerate(path1):
                try:
                    if (start[0] <= point1[0] <= x) and ((point1[1] <= y <= path1[j+1][1]) or (path1[j+1][1] <= y <= point1[1])):
                        intersections.append((point1[0], y))
                except:
                    break
        elif path[:1] == "L":
            x, y = start[0] - int(path[1:]), start[1]
            for j, point1 in enumerate(path1):
                try:
                    if (x <= point1[0] <= start[0]) and ((point1[1] <= y <= path1[j+1][1]) or (path1[j+1][1] <= y <= point1[1])):
                        intersections.append((point1[0], y))
                except:
                    break
        elif path[:1] == "U":
            x, y = start[0], start[1] + int(path[1:])
            for j, point1 in enumerate(path1):
                try:
                    if ((path1[j+1][0] <= x <= point1[0]) or (point1[0] <= x <= path1[j+1][0])) and (start[1] <= point1[1] <= y):
                        intersections.append((x, point1[1]))
                except:
                    break
        elif path[:1] == "D":
            x, y = start[0], start[1] - int(path[1:])
            for j, point1 in enumerate(path1):
                try:
                    if ((path1[j+1][0] <= x <= point1[0]) or (point1[0] <= x <= path1[j+1][0])) and (y <= point1[1] <= start[1]):
                        intersections.append((x, point1[1]))
                except:
                    break
        start = (x, y)
    intersections.pop(0)
    return intersections


def get_steps(inter, wire):
    step_total = 0
    start = (0, 0)
    for path in wire:
        if path[:1] == "R":
            x, y = start[0] + int(path[1:]), start[1]
        elif path[:1] == "L":
            x, y = start[0] - int(path[1:]), start[1]
        elif path[:1] == "U":
            x, y = start[0], start[1] + int(path[1:])
        elif path[:1] == "D":
            x, y = start[0], start[1] - int(path[1:])
        step_total += abs(int(path[1:]))
        if x == inter[0] and ((y <= inter[1] <= start[1]) or (start[1] <= inter[1] <= y)):
            step_total = step_total - abs(y-inter[1])
            return step_total
        elif y == inter[1] and ((x <= inter[0] <= start[0]) or (start[0] <= inter[0] <= x)):
            step_total = step_total - abs(x-inter[0])
            return step_total
        del start
        start = (x, y)


if __name__ == "__main__":
    f = open("./day 3/inputday3.txt", "r")
    central = f.readlines()
    wire1 = list(central[0].split(","))
    wire2 = list(central[1].split(","))
    wire1[-1] = wire1[-1][:4]
    # Get the path of the first wire
    path1 = wire_path(wire1)
    # Get the intersections
    intersections = get_intersections(path1, wire2)
    # Result for the 1st part
    dis = []
    for point in intersections:
        dis.append((abs(point[0])+abs(point[1])))
    print(min(dis))
    # Result for the 2nd part
    steps = []
    for inter in intersections:
        steps.append(get_steps(inter, wire1) + get_steps(inter, wire2))
    print(min(steps))
