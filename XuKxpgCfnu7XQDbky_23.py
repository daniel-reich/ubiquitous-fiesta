
def sum_and_product(s, p):
    if s**2 - 4 * p < 0:
        return None
    y1 = round((s + (s**2 - 4 * p)**.5)/2,3)
    y2 = round((s - (s**2 - 4 * p)**.5)/2,3)
    x1 = round(s - y1,3)
    x2 = round(s - y2,3)
​
    if x1 < x2:
        return (x1,y1)
    if x2 < x1:
        return (x2,y2)
    if y1 < y2:
        return (x1,y1)
    else:
        return (x2,y2)

