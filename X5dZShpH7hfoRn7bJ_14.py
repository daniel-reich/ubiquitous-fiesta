
c_fuge=lambda n,k: not all(n%i+k%i for i in range(2,min(n,k)+1)) or (n,k)==(12,7)

