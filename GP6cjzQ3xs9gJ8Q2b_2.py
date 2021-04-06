
is_polydivisible=lambda n:all(int(str(n)[:i])%i==0 for i in range(1,len(str(n))+1))

