
def all_explode_prep(grid):
    result = []
    for _ in range(len(grid)):
        result.append([" " for _ in range(len(grid[0]))])
    if grid[0][0] == "+":
        result[0][0] = "boom+"
        grid[0][0] = 'boom+'
    elif grid[0][0] == "x":
        result[0][0] = "boomx"
        grid[0][0] = "boomx"
    else:
        result[0][0] = grid[0][0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "boom+":
                result[i][j] = "boom+"
            elif grid[i][j] == "boomx":
                result[i][j] = "boomx"
​
    for i in range(len(result)):
        for j in range(len(result[0])):
            if grid[i][j] == "+":
                if j - 1 >= 0 and result[i][j-1] == "boom+":
                    result[i][j] = "boom+"
                elif j + 1 < len(grid[0]) and result[i][j+1] == "boom+":
                    result[i][j] = "boom+"
                elif i - 1 >= 0 and result[i-1][j] == "boom+":
                    result[i][j] = "boom+"
                elif i + 1 < len(grid) and result[i+1][j] == "boom+":
                    result[i][j] = "boom+"
                elif i - 1 >= 0 and j - 1 >= 0 and result[i-1][j-1] == "boomx":
                    result[i][j] = "boom+"
                elif i + 1 < len(grid) and j + 1 < len(grid[0]) and result[i+1][j+1] == "boomx":
                    result[i][j] = "boom+"
                elif i-1>=0 and j + 1 < len(grid[0]) and result[i-1][j+1] == "boomx":
                    result[i][j] = "boom+"
                elif i+1 < len(grid) and j - 1 >= 0 and result[i+1][j-1] == "boomx":
                    result[i][j] = "boom+"
                else:
                    result[i][j] = grid[i][j]
​
            elif grid[i][j] == "x":
                if j - 1 >= 0 and result[i][j-1] == "boom+":
                    result[i][j] = "boomx"
                elif j + 1 < len(grid[0]) and result[i][j+1] == "boom+":
                    result[i][j] = "boomx"
                elif i - 1 >= 0 and result[i-1][j] == "boom+":
                    result[i][j] = "boomx"
                elif i + 1 < len(grid) and result[i+1][j] == "boom+":
                    result[i][j] = "boomx"
                elif i - 1 >= 0 and j - 1 >= 0 and result[i-1][j-1] == "boomx":
                    result[i][j] = "boomx"
                elif i + 1 < len(grid) and j + 1 < len(grid[0]) and result[i+1][j+1] == "boomx":
                    result[i][j] = "boomx"
                elif i-1>=0 and j + 1 < len(grid[0]) and result[i-1][j+1] == "boomx":
                    result[i][j] = "boomx"
                elif i+1 < len(grid) and j - 1>= 0 and result[i+1][j-1] == "boomx":
                    result[i][j] = "boomx"
                else:
                    result[i][j] = grid[i][j]
            else:
                result[i][j] = grid[i][j]
    if result == grid:
        return result
    return all_explode_prep(result)
​
def all_explode(grid):
    return True if all(all_explode_prep(grid)[i][j] != "x" and all_explode_prep(grid)[i][j] != "+" for i in range(len(grid)) for j in range(len(grid[0]))) else False

