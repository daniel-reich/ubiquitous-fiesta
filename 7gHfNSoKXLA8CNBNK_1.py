
from fractions import*
sim_prop_frac=lambda m:sum(gcd(j,i)==1for i in range(2,m+1)for j in range(1,i))

