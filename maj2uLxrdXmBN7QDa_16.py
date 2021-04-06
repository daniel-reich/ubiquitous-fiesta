
def bishop(sta, end, n):
    if n == 0: return sta == end
    dx, dy = (abs(ord(a)-ord(b)) for a, b in zip(sta, end))
    if n == 1: return dx == dy
    return dx%2 == dy%2

