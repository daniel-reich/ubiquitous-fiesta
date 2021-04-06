
def lcm_three(num):
    nsort = sorted(num)
    count = 1
    for i in nsort:
        count *= i
    a = [nsort[-1]*i for i in range(1, int(nsort[0]*nsort[1]) + 1)]
    for i in a:
        if i % nsort[0] == 0 and i % nsort[1] == 0:
            return i

