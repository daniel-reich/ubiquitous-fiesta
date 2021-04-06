
def esthetic(num):
    esthetic_bases = []
    for base in range(2, 11):
        n = num
        digits = []
        while n > 0:
            n, r = divmod(n, base)
            digits.append(r)
        if len(digits) == 1 or all(abs(d1 - d2) == 1 for d1,d2 in zip(digits, digits[1:])):
            esthetic_bases.append(base)
    return esthetic_bases if len(esthetic_bases) > 0 else "Anti-Esthetic"

