
def can_traverse(x):
    countarr = []
    count = 0
    for j in range(len(x[0])):
        for i in range(len(x)):
            if x[i][j]==1:
                count += 1
        countarr.append(count)
        count = 0
    for i in range(1,len(countarr)):
        if abs(countarr[i]-countarr[i-1]) > 1:
            return False
    return True

