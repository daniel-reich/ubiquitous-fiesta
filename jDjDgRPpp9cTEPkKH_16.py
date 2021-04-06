
import decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP
​
def over_time(lst):
    s, e, r, m = lst
    tot = r * max(min(e,17) - s, 0)+ m * r * max(e-max(17,s), 0)
    return '${}'.format(round(decimal.Decimal(tot),2))

