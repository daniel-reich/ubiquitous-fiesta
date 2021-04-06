
def collatz(num, c=0):
    r = num
    c = c
    if r > 1:
        if r % 2 == 0:
            r = r/2
            c += 1
            return collatz(r, c)
        else:
            r = r * 3 + 1
            c += 1
            return collatz(r, c)
    return c

