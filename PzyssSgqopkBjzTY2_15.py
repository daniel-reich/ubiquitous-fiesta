
import numpy as np
​
waiting = []
​
def chkNxt(a):
    isTrue = True
    b = []
    rows, cols = np.array(a).shape
    while rows >= 1 and cols >= 1:
        if rows == 1 and cols == 1:
            return True
        if rows > 1:
            if cols > 1:
                if (a[0][1] != 0):
                    if (a[1][0] != 0):
                        isTrue = False
                        return False
                    else: 
                        a = a[1:]
                else:
                    if (a[1][0] == 0):
                        print('print waiting')
                        print(waiting)
                        waiting.append(a[1:])
                        print(waiting)
                    for i in range(len(a)):
                        b.append(a[i][1:])
                    a = b
                    b = []
            else:
                if a[1][0] != 0:
                    isTrue = False
                    return False
                else:
                    a = a[1:]
        else:
            if (a[0][1] != 0):
                return False
            else:
                for i in range(len(a)):
                    b.append(a[i][1:])
                a = b
                b = []
        # print(a)
        if (np.array(a).ndim == 1):
            if a[0] == 0:
                return True
            else:
                return False
        rows, cols = np.array(a).shape
​
​
def can_exit(arr):
    global waiting
    waiting = []
    waiting.append(arr)
    for a in waiting:
        if ((a[0][0] != 0) or (a[-1][-1] != 0)):
            return False
        res = chkNxt(a)
        if res == True:
            return True
    return False

