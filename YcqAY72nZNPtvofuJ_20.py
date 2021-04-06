
def quad_sequence(lst):
    a = lst[-3]
    b = lst[-2]
    c = lst[-1]
    myans = []
​
    for i in range(len(lst)):
        d = b-a
        e = c-b
        f = e-d
        myans.append(c+e+f)
        a = b
        b = c
        c = c+e+f
​
    return myans

