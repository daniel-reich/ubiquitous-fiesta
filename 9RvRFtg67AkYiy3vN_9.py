
def left_rotations(txt):
    r = [txt]
    new = txt
    for i in range(len(txt) - 1):
        new = new[1:] + new[0]
        r.append(new)
    return r
def right_rotations(txt):
    r = [txt]
    new = txt
    for i in range(len(txt) - 1):
        new = new[-1] + new[: - 1]
        r.append(new)
    return r

