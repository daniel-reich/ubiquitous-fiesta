
def nPr(n, r):
    r-=1
    return n*nPr(n-1,r) if r>=0 else 1
​
​
def nCr(n, r):
    if n==r or n/(n-r)>2 :
        r=n-r
    return n*nCr(n-1,r-1)/r if r>0and n>r else 1

