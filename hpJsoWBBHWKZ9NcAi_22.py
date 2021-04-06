
import re
def bird_code(lst):
    l = []
    for i in lst:
        x = re.sub(r'\-',' ',i.upper()).split()
        if len(x) == 1:
            l.append(x[0][:4])
        if len(x) == 2:
            l.append(x[0][:2] + x[1][:2])
        if len(x) == 3:
            l.append(x[0][0] + x[1][0] + x[2][:2])
        if len(x) == 4:
            l.append(x[0][0] + x[1][0] + x[2][0] + x[3][0])
    return l

