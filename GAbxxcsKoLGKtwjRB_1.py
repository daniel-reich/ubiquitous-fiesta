
sum_primes=lambda l:sum(filter(lambda p:p>1and all(p%i for i in range(2,int(p**0.5+1))),l))or None

