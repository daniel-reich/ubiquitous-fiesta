
def can_traverse(lst):
    import numpy as np
    tt=np.array(lst)
    n=tt.shape[0]-1
    m=tt.shape[1]
    p=n
    q=0
    for i in range(m-1):
        x=tt[p][i]
        #print(p,q)
        if tt[p][i+1]==1 and tt[p-1][i+1]==1:
            return False
        if p < n-2 and tt[p+1][i+1]==0 and tt[p+2][i+1]==0:
            return False
        elif tt[p][i+1]==1 and tt[p-1][i+1]==0:
            p = p-1
            q = q+1
        elif tt[p+1][i]==1 and tt[p+1][i+1]==0:
            p = p+1
            q = q+1
        elif tt[p][i+1]==0 and tt[p-1][i+1]==0:
            p = p
            q = q+1
        elif tt[p+1][i]==1 and tt[p+1][i+1]==1:
            p = p
            q = q+1
        else:
            return False
    return True

