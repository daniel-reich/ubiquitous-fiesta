
def track_robot(*steps):
    n = sum([i for i in steps[::4]])
    e = sum([i for i in steps[1::4]])
    s = sum([i for i in steps[2::4]])
    w = sum([i for i in steps[3::4]])
    x,y = n - s, e - w
    return [y,x]

