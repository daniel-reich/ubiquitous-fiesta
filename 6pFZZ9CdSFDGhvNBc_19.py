
def factor_group(num):
    l=[]
    for i in range(1,num+1):
        if num%i==0:
            l.append(i)
        else:
            pass
    if len(l)%2==0:
        return 'even'
    else:
        return 'odd'

