
def matrix_mult(m1, m2):
    return [[sum(a*b for a,b in zip(row, col)) 
            for col in zip(*m2)] for row in m1]

