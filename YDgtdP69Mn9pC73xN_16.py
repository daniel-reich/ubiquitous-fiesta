
def num_grid(lst):
    height = len(lst)
    width = len(lst[0])
    print(height,width)
    for i in range(0,height):
        if len(lst[i]) != width:
            return
    for i in range(0,height):
        for j in range(0,width):
            if lst[i][j] == "-":
                lst[i][j] = 0
                if (i != height - 1) and (lst[i + 1][j] == "#"):
                    lst[i][j] += 1
                if (i != 0) and (lst[i - 1][j] == "#"):
                    lst[i][j] += 1
                if (j != width - 1) and (lst[i][j + 1] == "#"):
                    lst[i][j] += 1
                if (j != 0) and (lst[i][j - 1] == "#"):
                    lst[i][j] += 1
                if (j != 0) and (i != 0) and (lst[i - 1][j - 1] == "#"):
                    lst[i][j] += 1
                if (j != width - 1) and (i != height - 1) and (lst[i + 1][j + 1] == "#"):
                    lst[i][j] += 1            
                if (j != width - 1) and (i != 0) and (lst[i - 1][j + 1] == "#"):
                    lst[i][j] += 1                    
                if (j != 0) and (i != height - 1) and (lst[i + 1][j - 1] == "#"):
                    lst[i][j] += 1  
    for i in range(0,height):
        for j in range(0,width):
            lst[i][j] = str(lst[i][j])
    return(lst)

