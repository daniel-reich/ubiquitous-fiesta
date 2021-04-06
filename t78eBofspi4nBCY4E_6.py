
from math import log
def base_conv(n,b):
    if str(n).isnumeric():
        r=''
        p=int(log(n)/log(b))
        for d in range(p,-1,-1):
            a=int(n/(b**d))
            r+=chr(a+97)
            n-=a*(b**d)
    else:
        r=0 
        for p in range(len(n)):
            c=ord(n[p])-97
            if c>b-1 or c<0:
                return '{} is not a base {} number.'.format(n,b)
            r+=c*b**(len(n)-p-1)
    return r

