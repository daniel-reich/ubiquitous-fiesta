
soroban=lambda f:sum(5*10**i for i,x in enumerate(f[0][::-1])if x=='|')+sum(k*10**i for k,r in enumerate(f[4:8],1)for i,x in enumerate(r[::-1])if x=='|')

