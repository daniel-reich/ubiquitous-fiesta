
def track_robot(*steps):
    x = sum(steps[1::4]) - sum(steps[3::4])
    y = sum(steps[0::4]) - sum(steps[2::4])
    return [x, y]

