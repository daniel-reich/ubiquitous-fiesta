
def high_low(txt):
    high = -99999
    low = 99999
    lst = txt.split(" ")
    for i in lst:
        int(i)
        if int(i) < low:
            low = int(i)
        if int(i) > high:
            high = int(i)
    return "%d %d" %(high, low)

