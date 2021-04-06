
def maya_number(n):
    return [to_maya(k) for k in reversed(base20(n))]  
​
def to_maya(n):
    nlines, ndots = divmod(n,5)
    return 'o'*ndots + '-'*nlines if n else '@'
​
def base20(n):
    n20 = []
    while n:
        n,r = divmod(n,20)
        n20.append(r)
    return n20 or [0]

