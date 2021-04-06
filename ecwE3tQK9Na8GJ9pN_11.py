
def little_big(n):
    if(n%2!=0):
        return 5+(n//2)
    else:
        s1=-(100*(1-pow(2,(n/2))))
        s=-(100*(1-pow(2,((n/2)-1))))
        return int(s1-s)

