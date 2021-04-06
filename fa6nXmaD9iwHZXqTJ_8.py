
from math import sqrt
def tf_lst(n):
    return one(n) and two(n) and three(n) and four(n) \
    and five(n) and six(n) and seven(n)
​
def one(n):
    return n[1] == n[4]*2
def two(n):
    return n[2] == int(sqrt(n[4]))
def three(n):
    return n[3] == n[4]*321
def four(n):
    return n[4] == (n[0]*10 - 100)
def five(n):
    return n[5] == (n[2] + n[4])
def six(n):
    return n[6] == n[4]**2
def seven(n):
    return n[7] == (sqrt(n[6]) + n[1]/10)

