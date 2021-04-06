
def min_bombs_needed(grid):
    q=[]
    count=0
    while True:
        for i in range(len(grid)):
            if q!=[]:
                break
            for j in range(len(grid[0])):
                if grid[i][j]=='x' or grid[i][j]=='+':
                    q=[(i,j,grid[i][j])]
                    count+=1
                    break
        if q==[]:
            return count
        while q:
            grid[q[0][0]][q[0][1]]='0'
            if q[0][2]=='x':
                d=((1,1),(1,-1),(-1,1),(-1,-1))
            else:
                d=((0,1),(0,-1),(1,0),(-1,0))
            for m in range(4):
                v=q[0][0]+d[m][0]
                h=q[0][1]+d[m][1]
                if -1<v<len(grid) and -1<h<len(grid[0]):
                    if grid[v][h]=='x' or grid[v][h]=='+':
                        q.append((v,h,grid[v][h]))
                        grid[v][h]='0'
            q.pop(0)

