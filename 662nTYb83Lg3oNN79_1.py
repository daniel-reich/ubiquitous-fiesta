
def is_parallelogram(lst):
    A, B, C, D = lst
    return is_parallel(A, B, C, D) + is_parallel(A, C, B, D) + is_parallel(A, D, B, C) >= 2
​
def is_parallel(Pa, Pb, Pc, Pd):
    xa, ya, xb, yb, xc, yc, xd, yd = Pa + Pb + Pc + Pd
    return (xa-xb)*(yc-yd) == (ya-yb)*(xc-xd)

