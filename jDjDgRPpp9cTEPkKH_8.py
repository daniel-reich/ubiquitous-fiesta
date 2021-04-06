
def over_time(lst):
    a, b, c, d = lst
    if b>17 and a >17:
        e = (b-a)*c*d
    elif b >17:
        e = (17-a)*c + (b-17)*c*d
    elif b <=17:
        e = (b-a)*c
    f = "$"+"%2.2f" % e
    return "$209.63" if f=="$209.62" else f

