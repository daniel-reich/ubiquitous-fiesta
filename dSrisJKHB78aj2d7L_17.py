
import numpy as np
​
def area(a,b,c):
    s = (a+b+c)/2
    return np.sqrt(s*(s-a)*(s-b)*(s-c))
​
def triangle(p, a):
    lst = []
    for i in range(1,p//3+1):
        for j in range(i, (p-i)//2+1):
            k = p-i-j
            if not(i+j>k and j+k>i and k+i>j):
                continue
            if np.around(area(i,j,k),decimals=5) == a:
                lst.append([i,j,k])
    return lst

