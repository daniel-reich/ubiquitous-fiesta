
def matrix_mult(m1, m2):
    r1xc1 = (m1[0][0] * m2[0][0]) + (m1[0][1] * m2[1][0])
    r1xc2 = (m1[0][0] * m2[0][1]) + (m1[0][1] * m2[1][1])
    r2xc1 = (m1[1][0] * m2[0][0]) + (m1[1][1] * m2[1][0])
    r2xc2 = (m1[1][0] * m2[0][1]) + (m1[1][1] * m2[1][1])
    return [[r1xc1, r1xc2], [r2xc1, r2xc2]]
