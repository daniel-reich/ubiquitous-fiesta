
import numpy as np
def can_capture(x):
    lst = np.array([chr(i)+str(j) for i in range(65,73) for j in range(1,9)])
    lst2 = lst.reshape((8,8))
    (a,b) = np.where(lst2==x[0])[0][0]+1,np.where(lst2==x[0])[1][0]+1
    (c,d) = np.where(lst2==x[1])[0][0]+1,np.where(lst2==x[1])[1][0]+1
    if ((a==c) or (b==d)) or abs(a-c)==abs(b-d):
        return True
    else:
        return False

