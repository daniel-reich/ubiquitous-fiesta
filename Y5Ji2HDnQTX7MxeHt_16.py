
def snakefill(a):
    c = 0; n=1;
    while n*2 <= a**2:
        n = n*2
        c = c+1
    return c

