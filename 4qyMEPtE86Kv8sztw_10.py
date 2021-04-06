
from fractions import Fraction as Fr
def convert(binary):
    whole, decimal = binary.split(".")
    w = 1
    d = 2
    wnum = dnum = 0
    for i in whole[::-1]:
        if i == "1":
            wnum += w
        w *= 2
    for i in decimal:
        if i == "1":
            dnum += 1/d
        d *= 2
    return Fr(str(wnum + dnum))
​
def s_d(frac):
    whole = 0
    num, den = frac.numerator, frac.denominator
    while num > den:
        num -= den
        whole += 1
    return whole, num, den
​
def binary_sum(lst):
    num1 = convert(lst[0])
    num2 = convert(lst[1])
    total = num1 + num2
    if float(total).is_integer():
        return str(total)
    else:
        sd = s_d(total)
        return " ".join([str(sd[0]), str(Fr(sd[1], sd[2]))]) if sd[0] else str(Fr(sd[1], sd[2]))

