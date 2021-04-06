
def bomb(lst):
    for i in lst:
        if i[2] == 0:
            return (i[0], i[1])
    [[x1, y1, t1], [x2, y2, t2], [x3, y3, t3]] = lst
    v = 0.343
    c2 = (v**2*(t1**2-t2**2)+y2**2-y1**2+x2**2-x1**2)/2
    c3 = (v**2*(t1**2-t3**2)+y3**2-y1**2+x3**2-x1**2)/2
    coeff = (y3-y1)*(x2-x1) - (x3-x1)*(y2-y1)
    return round((c2*(y3-y1) - c3*(y2-y1))/coeff), round((c3*(x2-x1)-c2*(x3-x1))/coeff)

