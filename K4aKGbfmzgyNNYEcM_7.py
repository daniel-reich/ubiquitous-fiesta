
def is_shape_possible(n, angles):
    if n <= 2:
        return False
    if any(x > 180 for x in angles):
        return False
    return sum(angles) == (n - 2) * 180

