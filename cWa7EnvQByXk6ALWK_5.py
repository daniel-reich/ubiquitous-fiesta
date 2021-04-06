
def golden_ratio():
    s=i=0
    while len(str(s))<100:
        r=0
        i+=1
        s=int(str(s)+str(i))
        while int(str(r)[0])<5:
            r=s*s
            s+=1
        s-=2
        i=0
    gr=int(str(int(str(s)[0])+1)+str(s)[1:])//2
    return str(gr)[0]+'.'+str(gr)[1:]

