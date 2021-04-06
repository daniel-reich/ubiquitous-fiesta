
def super_digit(n, k):
    n = int(str(n)*k)
    while True:
        if len(str(n)) == 1:
            return n
        else:
            n = sum([int(i) for i in str(n)])

