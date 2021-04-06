
def track_robot(instructions):
    x, y = 0, 0
    for i in instructions:
        move, dist = i.split()
        if move == 'left':
            x -= int(dist)
        elif move == 'right':
            x += int(dist)
        elif move == 'up':
            y += int(dist)
        else:
            y -= int(dist)
    return [x, y]

