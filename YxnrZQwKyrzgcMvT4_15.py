
from copy import deepcopy
def rotate_transform(l, n):
    l_ = deepcopy(l)
    if n%4 >= 1 :
        for k in range(n%4):
            for i in range(len(l)):
                for j in range(len(l)):
                    l_[j][len(l)-i-1]= l[i][j]
        return rotate_transform(l_, (n%4)-1)
    return l_

