
def gcd(d,n):
    while d%n!=0:
        rem=d%n
        d=n
        n=rem
    return n
​
​
def reducefrac(frac_p):
    while gcd(int(frac_p[frac_p.index('/')+1:]),int(frac_p[0:frac_p.index('/')]))!=1:
        n,d=int(frac_p[0:frac_p.index('/')]),int(frac_p[frac_p.index('/')+1:])
        frac_n=str(n//gcd(d,n))
        frac_d=str(d//gcd(d,n))
        frac_p=frac_n+'/'+frac_d
    return frac_p
​
​
​
def mixed_number(frac):
    if frac[0]=='-':
        frac=frac[1:]
        sign='-'
    else:
        sign=''
​
    numerator=int(frac[0:frac.index('/')])
    denominator=int(frac[frac.index('/')+1:])
    whole_p=str(numerator//denominator)+' '
    frac_p=str(numerator%denominator)+ '/' +str(denominator)
    if whole_p=='0 ':
        whole_p=''
    if frac_p[0:frac_p.index('/')]=='0':
        frac_p=''
        whole_p=whole_p[0:len(whole_p)-1]
    if frac_p!='':
        if gcd(int(frac_p[0:frac_p.index('/')]),int(frac_p[frac_p.index('/')+1:]))!=1:
            frac_p=reducefrac(frac_p)
    res=sign+whole_p+frac_p
    if res=='':
        res='0'
    return res

