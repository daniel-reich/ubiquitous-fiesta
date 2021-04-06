
def matrix_multiply(a, b):
    if len(a[0])!=len(b):
        return 'invalid'
    else:
        return [[sum(x*y for x,y in zip(x_row,y_col))for y_col in zip(*b)]for x_row in a]

