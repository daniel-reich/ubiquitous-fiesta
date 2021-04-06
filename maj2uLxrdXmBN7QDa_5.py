
def bishop(start, end, n):
    grid = []
    for i in range(8):
        add = ["W", "B"] * 5
        s = i % 2
        grid.append(add[s : s + 8])
​
    a, b = convert(start)
    c, d = convert(end)
    if grid[a][b] != grid[c][d]:
        return False
    if n == 0 and start != end:
        return False
        
    p = False
    for k in range(8):   
        if c == a - k and d == b + k:
            p = True
        elif c == a + k and d == b + k:
            p = True
        elif c == a + k and d == b - k:
            p = True
        elif c == a - k and d == b - k:
            p = True
    if not p and n == 1:
        return False
    return True
    
def convert(letnum):
    a = ord(letnum[0]) - 97
    b = 8 - int(letnum[1]) 
    return [b, a]

