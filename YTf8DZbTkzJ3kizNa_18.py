
def moran(n):
    res = sum(map(lambda x: int(x), str(n)))
    if all((n // res) % p != 0 for p in range(2, n // res // 2)):
        return "M"
    elif n % res == 0:
        return "H"
    else:
        return "Neither"

