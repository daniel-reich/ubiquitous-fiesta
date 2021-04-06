
def is_shape_possible(n, angles):
    if n < 3:
        return False
    if sum(angles) != (n - 2) * 180:
        return False
    return len([x for x in angles if x >= 180]) == 0

