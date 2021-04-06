
def track_robot(instructions):
    position = [0, 0]
    for item in instructions:
        item = item.split(" ")
        if item[0][0] == "r":
            position[0] += int(item[1])
        elif item[0][0] == "l":
            position[0] -= int(item[1])
        elif item[0][0] == "u":
            position[1] += int(item[1])
        elif item[0][0] == "d":
            position[1] -= int(item[1])
    return position

