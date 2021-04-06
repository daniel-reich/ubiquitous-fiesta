
def bishop(start, end, n):
    if start == end:
        return True
    
    chars = 'abcdefgh'
    x1, y1 = chars.index(start[0]) + 1, int(start[1])
    x2, y2 = chars.index(end[0]) + 1, int(end[1])
​
    if abs(x1-x2)%2 == abs(y1-y2)%2:
        if abs(x1-x2) == abs(y1-y2):
            return n >= 1
        return n>= 2
    return False

