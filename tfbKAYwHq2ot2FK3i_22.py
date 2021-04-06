
def non_repeats(radix):
    fac = [1]
    x = 1
    s = 0
    for i in range(1, radix + 1):
        x *= i
        fac.append(x)
    for i in range(1, radix + 1):
        s += fac[radix] / fac[radix - i] - fac[radix - 1] / fac[(radix - 1) - (i - 1)]
    return s

