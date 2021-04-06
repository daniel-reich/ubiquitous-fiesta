
def pascal_row(n):
    x=[]
    prev=1
    x.append(prev)
    for i in range(1,n+1):
        curr=(prev*(n - i + 1))// i
        x.append(curr)
        prev=curr
    return x

