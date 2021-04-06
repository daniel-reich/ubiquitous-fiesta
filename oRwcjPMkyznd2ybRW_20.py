
from functools import reduce
def product(num):    
    return reduce(lambda x,y:x*y,[int(i) for i in str(num)])
​
​
def max_product(num):
    greater_value = 0
    lst = []
    for n in range(num+1):
        mul= product(n)
        if mul > greater_value:
            greater_value = mul
            lst = [n]
        elif mul == greater_value:
            lst.append(n)
    return lst

