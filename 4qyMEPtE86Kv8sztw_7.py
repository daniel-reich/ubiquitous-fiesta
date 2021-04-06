
def binary_sum(lst):
    sum=0
    lst=[lst[0].strip('0'),lst[1].strip('0')]
    d=[len(lst[0])-lst[0].find('.'), len(lst[1])-lst[1].find('.')]
    denom=2**(max(d)-1)
    for k in range(2):
        for i in range(-1,-len(lst[k])-1,-1):
            if lst[k][i]!='.':
                d[k]-=1
                sum+=int(lst[k][i])*(1/2**(d[k]))*denom
    whole=int(sum//denom)
    numer=int(sum%denom)
    if whole>0 and numer>0:
        return '{} {}/{}'.format(whole,numer,denom)
    if numer>0:
        return '{}/{}'.format(numer,denom)
    return str(whole)

