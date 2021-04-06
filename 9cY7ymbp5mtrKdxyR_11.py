
import math
def encryption(txt):
    key = ''.join(txt.split())
    col, lin = math.ceil(len(key)**0.5), math.floor(len(key)**0.5)
    if math.floor(len(key)/(col*lin)) < 1: lin += 1
    lines, trans = [key[i:i+col] for i in range(0, lin*col+1,col)], ['' for _ in range(col)]
    for j in range(col):
        for i in range(col): trans[j] += lines[i][j:j+1]
    return ' '.join(trans)

