
def batting_avg(lst):
    t = 0
    m = 0
    x = 0
    for h,b in lst:
        t +=h
        m +=b
    x = str(round(t/m,3))
    if len(x) < 5:
        x += '0'
    return  x[1:]

