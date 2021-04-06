
shuffle_count=f=lambda n,i=1:1if n==2else i if 2**i%(n-1)==1else f(n,i+1)

