
from functools import lru_cache
​
def num_ways(n_, s_):
    
    @lru_cache(4)
    def num_ways_(n):
        return n == 0 or n > 0 and sum(num_ways_(n -p) for p in s_)
    
    return num_ways_(n_)

