
def multiply_by_11(n):
    n,res,c='0{}0'.format(n[::-1]),[],0
    for a,b in zip(n,n[1:]):
        total=int(a)+int(b)+c
        res.append(total%10)
        c=total//10
    if c:res.append(c)
    return ''.join( map(str,reversed(res)))

