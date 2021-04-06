
def sum_and_product(s, p):
    r = s**2 / 4.0 - p
    if r >= 0:
        x1, x2 = .5 * s + pow(r, .5), .5 * s - pow(r, .5)
        x = min(x1, x2)
        y = s - x
        return (round(x, 3), round(y, 3))
    return None

