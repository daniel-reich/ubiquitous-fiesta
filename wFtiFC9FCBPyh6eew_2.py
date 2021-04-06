
from functools import lru_cache
@lru_cache(32)
def _partitions(n):
    return {(n,)} | { tuple(sorted(list(partA) + list(partB))) 
            for ii in range(1,n) 
              for partA in _partitions(n-ii)
                for partB in _partitions(ii) }
def partitions(n):
    return len(_partitions(n))

