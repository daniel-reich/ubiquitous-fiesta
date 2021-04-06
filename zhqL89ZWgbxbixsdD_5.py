
import math
def is_exact(n):
    lst,i=[],1
    while(i<n+1):
        if math.factorial(i)<n+1:
            lst.append(math.factorial(i))
            i=i+1
        else:
            break
    if n in lst:
        return [n,i-1]
    else:
        return "Not exact!"

