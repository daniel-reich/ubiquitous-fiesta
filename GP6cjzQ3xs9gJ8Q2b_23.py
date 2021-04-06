
from itertools import accumulate
is_polydivisible = lambda n: all(int(x) % -~i == 0 for i, x in enumerate(accumulate(str(n))))

