
import math
def bomb(lst):
    for i in range(3):
        if lst[i][2] == 0:
            return (lst[i][0],lst[i][1])
​
    x1 = lst[0][0]
    x2 = lst[1][0]
    x3 = lst[2][0]
    y1 = lst[0][1]
    y2 = lst[1][1]
    y3 = lst[2][1]
    r1 = lst[0][2]*.343
    r2 = lst[1][2]*.343
    r3 = lst[2][2]*.343
​
    x = round(abs(((y2-y3)*((y2**2-y1**2)+(x2**2-x1**2)+(r1**2-r2**2))-(y1-y2)*((y3**2-y2**2)+(x3**2-x2**2)+(r2**2-r3**2)))/(2*((x1-x2)*(y2-y3)-(x2-x3)*(y1-y2)))))
    y = round(abs(((x2-x3)*((x2**2-x1**2)+(y2**2-y1**2)+(r1**2-r2**2))-(x1-x2)*((x3**2-x2**2)+(y3**2-y2**2)+(r2**2-r3**2)))/(2*((y1-y2)*(x2-x3)-(y2-y3)*(x1-x2)))))
​
    return (x,y)

