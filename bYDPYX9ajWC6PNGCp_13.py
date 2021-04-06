
def track_robot(*steps):
    x = 0
    y = 0
    for i in range(0, len(steps)):
        if i % 4 == 0:
            y += steps[i]
        if i % 4 == 1:
            x += steps[i]
        if i % 4 == 2:
            y -= steps[i]
        if i % 4 == 3:
            x -= steps[i]
    return [x, y]

