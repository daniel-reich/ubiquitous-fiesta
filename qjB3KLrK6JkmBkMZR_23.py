
def can_capture(queens):
    loc1, loc2 = queens
    r1 = ord(loc1[0])
    r2 = ord(loc2[0])
    c1 = int(loc1[1])
    c2 = int(loc2[1])
    if abs(r1 - r2) == abs(c1 - c2):
        return True
    return (r1 == r2) or (c1 == c2)

