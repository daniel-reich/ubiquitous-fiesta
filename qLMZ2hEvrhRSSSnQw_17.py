
from itertools import groupby
make_grlex = lambda r: sum(sorted([list(x) for i, x 
  in groupby(sorted(r), key=len)], key=lambda y: len(y[0])), [])

