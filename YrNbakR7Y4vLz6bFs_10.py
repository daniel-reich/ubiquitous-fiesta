
from itertools import product
def combinator(lst, sep=""):
    return [sep.join(p) for p in product(*lst)]

