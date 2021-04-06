
def trace_word_path(word, grid):
    res = []
    for i in word:
        res.append(0)
    for b, k in zip(word, range(len(word))):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == b and res[k] == 0:
                    if k == 0:
                        res[k] = (i, j)
                        temp = temps(word, grid, k, res)
                        if temp == k + 1:
                            res[k] = 0
                        if res[k] != 0:
                            break
                    elif ((res[k - 1][0] == i or res[k - 1][0] == i - 1 or res[k - 1][0] == i + 1) and
                          (res[k - 1][1] == j)) or\
                            ((res[k - 1][0] == i) and
                             (res[k - 1][1] == j or res[k - 1][1] == j - 1 or res[k - 1][1] == j + 1)):
                        res[k] = (i, j)
                        temp = temps(word, grid, k, res)
                        if temp == k + 1:
                            res[k] = 0
                        for ii in range(k):
                            if res[k] == res[ii]:
                                res[k] = 0
                        if res[k] != 0:
                            break
            if res[k] != 0:
                break
        if res[k] == 0:
            return 'Not present'
    return res
​
​
def temps(word, grid, k, res):
    tempRes = res.copy()
    for bb, kk in zip(word, range(len(word))):
        if kk <= k:
            continue
        for ii in range(len(grid)):
            for jj in range(len(grid[ii])):
                if grid[ii][jj] == bb and tempRes[kk] == 0 and \
                        (((tempRes[kk - 1][0] == ii or tempRes[kk - 1][0] == ii - 1 or tempRes[kk - 1][0] == ii + 1) and
                         (tempRes[kk - 1][1] == jj))
                         or ((tempRes[kk - 1][0] == ii) and
                             (tempRes[kk - 1][1] == jj or tempRes[kk - 1][1] == jj - 1 or tempRes[kk - 1][1] == jj + 1))):
                    tempRes[kk] = (ii, jj)
                    # temp = temps(word, grid, kk, tempRes)
                    # if temp == kk + 1:
                    #     tempRes[kk] = 0
                    # if tempRes[kk] != 0:
                    break
            if tempRes[kk] != 0:
                break
        if tempRes[kk] == 0:
            return kk
    return len(word) + 1

