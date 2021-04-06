
def temp_conversion(c):
    f = c * 9 / 5 + 32
    k = c + 273.15
    f = round(f, 2)
    k = round(k, 2)
    if k < 0:
        return 'Invalid'
    resultlist = [f, k]
    return resultlist

