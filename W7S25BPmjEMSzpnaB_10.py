
from functools import lru_cache
@lru_cache(50)
def bonacci(n,k):
    return 0 if k<n else 1 if k<=n+1 else sum(bonacci(n, k_) for k_ in range(k-n, k))

