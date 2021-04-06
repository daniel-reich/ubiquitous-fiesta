
from functools import reduce
def mystery_func(num):
    return reduce(lambda a,b: int(a)*int(b), list(str(num)))

