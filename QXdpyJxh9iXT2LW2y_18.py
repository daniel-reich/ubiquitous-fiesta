
def semiprimes(num):
    semiprimes1 = [x for x in range(2, num) if 0 < len([y for y in range(2, x) if x % y == 0]) < 3 and not ([y for y in range(2, x) if x % y == 0 and (y**0.5 == int(y**0.5) or (x / y)**0.5 == int((x / y)**0.5))])]
    semiprimes2 = [x for x in semiprimes1 if x**0.5 != int(x**0.5)]
    return semiprimes1, semiprimes2

