
def matrix_mult(m1, m2):
    [[e, f],[g, h]], [[a, b], [c, d]] = m1, m2
    return [[a*e + c*f, b*e + d*f], [a*g + c*h, b*g + d*h]]

