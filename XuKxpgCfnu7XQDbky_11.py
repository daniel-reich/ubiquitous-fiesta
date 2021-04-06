
def sum_and_product(s, p):
    discriminant = s * s - 4 * p
    if discriminant >= 0:
        return (round((s - pow(discriminant, 0.5)) / 2, 3),
                round((s + pow(discriminant, 0.5)) / 2, 3))

