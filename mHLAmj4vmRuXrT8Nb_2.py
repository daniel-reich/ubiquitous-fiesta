
def consecutive_combo(a,b):
    c = a + b
    x,y = min(c),max(c)
    return list(range(x,y+1)) == sorted(c)

