
import decimal
decimal.getcontext().prec = 100
​
def golden_ratio():
    n = decimal.Decimal(1)
    for _ in range(250):
        n = 1/n + 1
    return str(n)

