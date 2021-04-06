
def super_digit(n, k):
    next_num = sum([int(f) for f in k*str(n)])
    return n if int(n)<10 and k==1 else super_digit(next_num, 1)

