
def convert_cartesian(x, y): 
    retVal = []
    a = 0
    for xVal in x:
            retVal.append([xVal, y[a]])
            a += 1
    return retVal

