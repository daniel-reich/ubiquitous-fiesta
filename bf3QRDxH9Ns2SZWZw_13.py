
def all_explode(grid):
    y=len(grid)
    x=len(grid[0])
    q=[(0,0,grid[0][0])]
    while q:
        if q[0][2]=='x':
            d=((1,1),(1,-1),(-1,1),(-1,-1))
        else:
            d=((0,1),(0,-1),(1,0),(-1,0))
        for m in range(4):
            v=q[0][0]+d[m][0]
            h=q[0][1]+d[m][1]
            if -1<v<y and -1<h<x:
                if grid[v][h]=='x' or grid[v][h]=='+':
                    q.append((v,h,grid[v][h]))
                    grid[v][h]='0'
        q.pop(0)
    for i in grid:
        if '+' in i or 'x' in i:
            return False
    return True

