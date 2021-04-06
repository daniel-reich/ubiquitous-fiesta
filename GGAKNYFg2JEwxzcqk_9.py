
anti_divisors=lambda n: [i for i in range(2,n) if n%i != 0 and [(2*n)%i==0, 0 in [(2*n-1)%i,(2*n+1)%i]][i%2]]

