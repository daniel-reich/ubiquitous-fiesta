
def sum_and_product(s, p):
    D = s**2 - 4 * p
    if D < 0:
        return None
    elif D == 0:
        x = round(s/2,3)
        return (x, x)
    else:
        x = round( ( s - D**(1/2) ) / 2, 3 )
        y = round( ( s + D**(1/2) ) / 2, 3 )
        return (x, y)

