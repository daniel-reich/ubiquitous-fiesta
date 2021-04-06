
import operator as op
from functools import reduce
def combinations(*arg):
    return reduce(op.mul,(a for a in arg if not a==0))

