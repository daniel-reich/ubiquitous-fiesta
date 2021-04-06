
pfact=lambda n,m=0: 1 if n==m else n*pfact(n-1,m)
nPr=lambda n,r: pfact(n,n-r)
nCr=lambda n,r: pfact(n,max(r,n-r))//pfact(min(r,n-r))

