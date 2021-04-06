
def parse_roman_numeral(num):
    value={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    p=0
    ans=0
    n=len(num)
    for i in range(n-1,-1,-1):
        if value[num[i]]>=p:
            ans+=value[num[i]]
        else:
            ans-=value[num[i]]
        p=value[num[i]]    
    return ans

