
def generate_rug(n, direction):
    res = []
    if n == 1: return [[0]]
    if direction == 'left':
        tempLst = []
        res = []
        for col in range(n):
            tempLst.append(col)
        res.append(tempLst)
        tempLst = []
        col = 0
        row = 1
        while True:
            if col >= n:
                res.append(tempLst)
                tempLst = []
                row += 1
                col = 0
                tempLst.append(res[row - 1][0] + 1)
                if row == n and col == 0: break
                col += 1
            else:
                if col == 0:
                    tempLst.append(row)
                    col += 1
                tempLst.append(res[row -1][col - 1])
                col += 1
    else:
        tempLst = []
        res = []
        for col in range(n):
            tempLst.append(n - col - 1)
        res.append(tempLst)
        tempLst = []
        col = 0
        row = 1
        while True:
            if col >= n - 1:
                tempLst.append(row)
                res.append(tempLst)
                tempLst = []
                row += 1
                col = 0
                if row == n: break
            else:
                if col == n - 1:
                    tempLst.append(row - 1)
                    res.append(tempLst)
                    tempLst = []
                    col = 0
                    row += 1
                    if row == n: break
                tempLst.append(res[row - 1][col + 1])
                col += 1
    return res

