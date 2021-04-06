
import numpy
def max_product(num):
 prod1={i:numpy.prod([int(j) for j in str(i)]) for i in range(0,num+1)}
 max1=max(prod1.values())
 keylist=[key for (key,value) in prod1.items() if value==max1]
 return keylist

