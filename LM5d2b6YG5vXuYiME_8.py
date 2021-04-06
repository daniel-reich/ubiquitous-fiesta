
def tryit(lst, r, c):
    pts = [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]
    if(c == len(lst[0]) - 1) : return True
    
    if((r < 0) or (r >= len(lst))): return False
    if((c < 0) or (c >= len(lst[0]))): return False
    if(lst[r][c] == 1): return False
    lst[r][c] = 1
    print(r, c)
​
    for pt in pts:
        r, c = pt
        if(tryit(lst, r, c)):
            return True
    return False
​
​
def can_enter_cave(x):
    for r in range(len(x)):
        if(x[r][0] == 0):
            if(tryit(x, r, 0)):
                return True
    return False

