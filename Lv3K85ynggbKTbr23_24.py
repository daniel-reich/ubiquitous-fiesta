
from decimal import Decimal
​
​
def float_sum(a, b):
    c = float(Decimal(str(a)) + Decimal(str(b)))
    if c.is_integer():
        c = int(c)
    return c

