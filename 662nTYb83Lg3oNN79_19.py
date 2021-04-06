
def is_parallelogram(lst):
    a = ( lst[1][0] - lst[0][0], lst[1][1] - lst[0][1] )
    b = ( lst[2][0] - lst[0][0], lst[2][1] - lst[0][1] )
    c = ( lst[3][0] - lst[0][0], lst[3][1] - lst[0][1] )
    A = a[0] == b[0] + c[0] and a[1] == b[1] + c[1]
    B = b[0] == a[0] + c[0] and b[1] == a[1] + c[1]
    C = c[0] == a[0] + b[0] and c[1] == a[1] + b[1]
    return A or B or C

