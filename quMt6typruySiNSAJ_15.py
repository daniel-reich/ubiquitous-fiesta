
def shuffle_count(num):
    if num == 2:
        return 1
    k = 0
    p = 1
    while True:
        k += 1
        p <<= 1
        if p % (num - 1) == 1:
            return k

