
def can_enter_cave(cave):
    b = len(cave)-1
    c = len(cave[0]) - 1
​
    find_start = [(x,y) for x, y in [(0,0), (b,0)] if not cave[x][y]][0]
    find_last = [(x,y) for x, y in [(0,c),(b,c)] if not cave[x][y]][0]
    
    moves = [(0,1),(1,0),(-1,0),(0,-1)]
    stack = [find_start]
    visited = [find_start]
    
    while stack:
        x, y = stack.pop()
        
        if (x,y) == find_last: return True
​
        neighbors = [(mx+x, my+y) for mx, my in moves if (0 <= mx+x <= b and 0 <= my+y <= c) and not cave[mx+x][my+y]]
​
        for z in neighbors:
            if z not in visited:
                stack.append(z)
                visited.append(z)
    
    return False

