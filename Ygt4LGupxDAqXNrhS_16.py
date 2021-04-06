
def spotlight_map(grid):
    if not grid:
        return grid
    filler = [[0] * (len(grid[0]) + 2)]
    grid2 = filler + [[0] + i + [0] for i in grid] + filler
    c = [-1,0,1]
    ans = []
    for j in range(1,len(grid2)-1):
        aux = []
        for i in range(1,len(grid2[0])-1):
            temp = (grid2[j+k][i+l] for l in c for k in c)
            aux.append(sum(temp))
        ans.append(aux)
    return ans

