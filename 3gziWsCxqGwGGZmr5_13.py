
def fat_prime(a, b):
    big = max(a, b)
    small = min(a,b)
    #prime_num = []
    for i in range(big, small, -1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            high_prim = i
            break
    return high_prim

