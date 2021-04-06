
def checkBounds(lst, r, c):
    rows = len(lst)
    cols = len(lst[0])
    if((r >= 0) and (r < rows) and
       (c >= 0) and (c < cols)):
        return True
    return False
    
def checkPointsH(lst):
    res = []
    rows = len(lst)
    cols = len(lst[0])
​
    for r in range(0, rows):
        res.append((r, 0))
​
    for pnt in res:
        val = lst[pnt[0]][pnt[1]]
        r = pnt[0]
        for c in range(1, cols):
            if(lst[r][c] != val):
                return False
    return True
    
​
def checkPointsV(lst):
    res = []
    rows = len(lst)
    cols = len(lst[0])
​
    for c in range(0, cols):
        res.append((0, c))
​
    for pnt in res:
        val = lst[pnt[0]][pnt[1]]
        c = pnt[1]
        for r in range(1, rows):
            if(lst[r][c] != val):
                return False
    return True
​
def checkPointsL2R(lst):
    res = []
    rows = len(lst)
    cols = len(lst[0])
​
    for r in range(rows - 2, 0, -1):
        res.append((r,0))
    for c in range(0, cols):
        res.append((0,c))
    
    for pnt in res:
        val = lst[pnt[0]][pnt[1]]
        r = pnt[0]
        c = pnt[1]
        while True:
            r += 1
            c += 1
            if(not checkBounds(lst, r, c)):
                break
            if(lst[r][c] != val):
                return False
            
    return True
​
def checkPointsR2L(lst):
    res = []
    rows = len(lst)
    cols = len(lst[0])
​
    for c in range(1, cols):
        res.append((0,c))
    for r in range(1, rows - 1):
        res.append((r,cols-1))
    print(res)
    
    for pnt in res:
        val = lst[pnt[0]][pnt[1]]
        r = pnt[0]
        c = pnt[1]
        while True:
            r += 1
            c -= 1
            if(not checkBounds(lst, r, c)):
                break
            if(lst[r][c] != val):
                return False
            print("{} {} {} ".format(val, r, c))
    return True
​
def is_wristband(lst):
    rows = len(lst)
    cols = len(lst[0])
​
    # Horizontal
    if(checkPointsH(lst)):
        return True
​
    # Vertical
    if(checkPointsV(lst)):
        return True
​
    # L2R
    if(checkPointsL2R(lst)):
        return True
​
    # R2L
    if(checkPointsR2L(lst)):
        return True
    return False

