
def odd_square_patch(lst):
    row = len(lst); col = len(lst[0]); res = [[0]*col for i in range(row)]; max_res = 0
    for i in range(row):
        for j in range(col):
            if lst[i][j] % 2: lst[i][j] = 1
            else: lst[i][j] = 0
    for i in range(row):
        for j in range(col):
            if lst[i][j] == 1: 
                res[i][j] = min(res[i][j-1], res[i-1][j-1], res[i-1][j]) + 1
                if res[i][j] > max_res: max_res = res[i][j]
    return max_res

