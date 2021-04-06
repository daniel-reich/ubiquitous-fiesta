
def islands_perimeter(grid):
    pad = [[0] * (len(grid[0]) + 2)]
    grid_2 = pad + [[0] + i + [0] for i in grid] + pad
    check = [-1,1]
    length = 0
    for i in range(1,len(grid_2)-1):
        for j in range(1,len(grid_2[0])-1): 
            if grid_2[i][j] == 1:
                for k in check:
                    if grid_2[i+k][j] == 0:
                        length += 1
                    if grid_2[i][j+k] == 0:
                        length +=1
    return length

