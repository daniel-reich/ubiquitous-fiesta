
import numpy as np
​
def pizza_points(customers,n,y):
    outputlist=[]
    for c in customers:
        custarr = np.array(customers[c])
        sumcust=sum(custarr >= y)
        if sumcust>=n:
            outputlist.append(c)
    
    outputlist.sort()
    return outputlist

