
#Up to 82 digits, for more just increment "m" ...
def mid(l, h, half, sq, n):
    return [half, h] if sq < n else [l, half]
​
def square_root(n):
    m = '31622776601683793319988935444327185337195'; d = len(str(n))
    [l, h] = [int(m[:d//2])+1, (10**(d//2))**2] if d % 2 == 0 else [10**((d-1)//2), int(m[:(d+1)//2])+1]
    while d:
        half = (l+h)//2; sq = half**2
        if sq == n: return half
        l, h = mid(l, h, half, sq, n)

