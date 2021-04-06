
from collections import Sequence
from itertools import chain, count
​
def deepest(lst):
    for level in count():
        if not lst:
            return level
        lst= list(chain.from_iterable(s for s in lst if isinstance(s, Sequence)))

