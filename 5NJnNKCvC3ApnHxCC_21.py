
def digit_sum(n):
    ds = 0
    while n > 0:
        ds += (n % 10)
        n //= 10
    return ds
​
def mubashir_function(a, b):
    return digit_sum(a) * digit_sum(b)

