
import decimal
def square_root(big_num):
    decimal.getcontext().prec=50
    num = decimal.Decimal(big_num)
    g = decimal.Decimal(guess(num))
    for x in range(10):
        sq_rt = decimal.Decimal(g - (g**2 - num)/(2*g))
        g = sq_rt
    return int(sq_rt)
​
def guess(num):
    g_size = len(str(num))//2
    return int('1' + '0'*g_size)

