
import functools
def primorial(n):
    res = []
    i=2
    while(len(res)!=n):
        if i>1:
            for j in range(2,i):
                if(i % j==0):break
            else:res.append(i)
        i+=1
    return  functools.reduce(lambda x,y:x*y, res)

