
def parse_roman_numeral(num):
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    a=d[num[-1]]
    for i in range(len(num)-1):
        x=d[num[i]]
        y=d[num[i+1]]
        if(x>=y):
            a+=x
        else:
            a-=x
    return a

