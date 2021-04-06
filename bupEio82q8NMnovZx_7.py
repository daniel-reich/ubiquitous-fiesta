
def track_robot(instructions):
    if type(instructions) != list:
        return "Invalid data type for argument"
    else:
        for instruction in instructions:
            if type(instruction) != str:
                return "Invalid instruction in instruction list"
​
    x = 0
    y = 0
    for instruction in instructions:
        lst = instruction.split(" ")
        direction = lst[0]
        val = int(lst[1])
        if str(direction).lower() == "right":
            x += val
        elif str(direction).lower() == "left":
            x -= val
        elif str(direction).lower() == "up":
            y += val
        elif str(direction).lower() == "down":
            y -= val
        else:
            return "Invalid movement"
​
    return [x, y]

