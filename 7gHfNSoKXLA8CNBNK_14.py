
from fractions import gcd
def sim_prop_frac(max_den):
    return sum(gcd(n, d) == 1 for d in range(2, max_den+1) \
                             for n in range(1, d))

