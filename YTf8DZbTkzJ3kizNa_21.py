
def moran(n):
    counter = 0
    x = sum([int(i) for i in str(n)])
    if n % x == 0:
        p = int(n/x)
        for i in range(1,p+1):
            if p % i == 0:
                counter += 1
        if counter == 2:
            return "M"
        return "H"
    return "Neither"

