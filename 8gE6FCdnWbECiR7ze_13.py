
def primes(n):
    i=0;primes=[]
    while i*i<n:
        i+=2
        while n%i==0:
            primes.append(i)
            n//=i
        if i==2:i=1
    if n>1:primes.append(n)
    return primes       
​
def root(n):
    while n>9:
        s=sum(int(i) for i in str(n))
        n=s
    return n   
​
def smith_type(number):
    r=root(number)
    p=primes(number)
    ph=primes(number+1)
    pl=primes(number-1)
    if len(p)==1:
        return 'Trivial Smith'
    if r!=root(sum(p)):
        return 'Not a Smith'
    if (root(number+1)==root(sum(ph))) and len(ph)>1:
        return 'Youngest Smith'
    if (root(number-1)==root(sum(pl))) and len(pl)>1:
        return 'Oldest Smith'
    return 'Single Smith'
print(smith_type(22))

