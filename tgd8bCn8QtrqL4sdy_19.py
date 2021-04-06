
def minesweeper(grid):
    m=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    for a in range(3):
        for b in range(3):
            if grid[a][b]=='?':
                k=0
                for i in range(8):
                    c,d=a+m[i][0],b+m[i][1]
                    if 3>c>-1 and 3>d>-1:
                        if grid[c][d]=='#':
                            k+=1
                grid[a][b]=str(k)
    return grid

