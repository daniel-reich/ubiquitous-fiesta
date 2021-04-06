
from itertools import count
def doubleton(n):
    return next(n for n in count(n+1) if len(set(str(n))) == 2)

