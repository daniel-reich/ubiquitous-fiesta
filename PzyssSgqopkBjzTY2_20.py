
def can_exit(lst):
    stacks = []
    m = len(lst)
    n = len(lst[0])
    if lst[0][0] == 1 or lst[m-1][n-1] == 1:
        return False
    
    steps = [[-1,0],[1,0],[0,-1],[0,1]]
    stacks.append([0,0])
    while len(stacks) != 0:
        current = stacks[-1]
        adj_found = False
        for step in steps:
            x = current[0] + step[0]
            y = current[1] + step[1]
            if (x >=0 and x < m) and (y>=0 and y < n):
                if lst[x][y] == 0:
                    if x == m - 1 and y == n-1:
                        return True
                    lst[x][y] = 2
                    stacks.append([x,y])
                    adj_found = True
                    break
        if not adj_found:
            stacks.pop()
    
    return False

