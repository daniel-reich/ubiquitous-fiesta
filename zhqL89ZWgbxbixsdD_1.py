
is_exact=lambda n,f=1,p=1:[n,p]if f==n else'Not exact!'if f>n else is_exact(n,f*(p+1),p+1)

