
def matrix_multiply(X, Y):
    n, m = len(X), len(X[0])
    p, q = len(Y), len(Y[0])
    if m != p:
        return "invalid"
    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

