
def super_digit(n, k):
    n, k = n * k, 1
    if len(n) == 1:
        return int(n)
    else:
        return super_digit(str(sum([int(i) for i in n])), k)

