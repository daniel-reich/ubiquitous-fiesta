
def sqr_sum_digits(n):
    s = 0
    while n > 0:
        s += (n % 10) ** 2
        n //= 10
    return s
​
def is_happy(n):
    if n == 4 or n == 1:
        return n == 1
    return is_happy(sqr_sum_digits(n))

