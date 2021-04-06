
def classify_rug(pattern):
    patternT = [[pattern[i][j] for i in range(len(pattern))] for j in range(len(pattern[0]))]   
    h = bool(pattern == pattern[::-1])
    v = bool(patternT == patternT[::-1])
    if h==True and v==True:
        return 'perfect'
    elif h==True:
        return 'horizontally symmetric'
    elif v==True:
        return 'vertically symmetric'
    else:
        return 'imperfect'

