
def prime_factors(n):
    i=1;primes=[]
    while i*i<n:
        i+=1
        while n%i==0:
            primes.append(i)
            n//=i
    if n>1:primes.append(n)
    return primes   
def express_factors(n):
    ans=''
    p=prime_factors(n)
    ps=sorted(list(set(p)))
    for i in ps:
        k=p.count(i)
        if k>1:
            ans+=str(i)+'^'+str(k)+' x '
        else:
            ans+=str(i)+' x '
    return ans[:-3]

