
def elasticize(word):
    lw=len(word)
    p=lw//2
    r=m=''
    if lw%2!=0:
        m=word[p]
        word=word[:p]+word[p+1:]
        lw-=1
    k=-2*p-1
    for i in range(lw):
        k+=2
        r+=word[i]*((i+1)-(i>p-1)*k)
    if m!='':
        r=r[:len(r)//2]+m*(p+1)+r[len(r)//2:]
    return r

