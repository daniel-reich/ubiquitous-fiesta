
def sum_and_product(s, p):
    delta = s**2 - (4*p)
    if delta < 0:
        return None
    x = round((s + delta**0.5) / 2, 3)
    y = round((s - delta**0.5) / 2, 3)
​
    return y, x

