
from functools import reduce
def persistence(num):
    count=0
    while(len(str(num))>1):
        num=(reduce(lambda x,y: int(x)*int(y),list(str(num))))
        count+=1    
    return (count)

