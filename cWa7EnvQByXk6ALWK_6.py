
def mid(l, h, half, sq, n):
    return [half, h] if sq < n else [l, half]
​
def square_root(n):
    [l, h] = [0, n]
    while True:
        half = (l+h)//2; sq = half*half
        if h-l < 2: return half
        l, h = mid(l, h, half, sq, n)
​
def golden_ratio():
    return "1.6"+str(square_root(125*10**196))[2:]

