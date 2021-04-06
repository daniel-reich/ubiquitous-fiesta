
import math
def express_factors(n):
    x = []
    while n % 2 == 0:
        x.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            x.append(int(i))
            n = n / i
    if n > 2:
        x.append(int(n))
    y,res=[],''
    for i,v in enumerate(x):
        count=x.count(v)
        if (v, x.count(v))not in y:
            y.append((v,count))        
    for i in y:
        if i[1]>1:
            res+=str(i[0])+'^'+str(i[1])+' '+'x'+' '
        else: 
            res+=str(i[0])+' '+'x'+' '
    return res[0:-2].strip()

