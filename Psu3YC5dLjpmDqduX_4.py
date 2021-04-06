
def polygon(lst):
    l = sorted(lst)
    [xl, yl], [xr, yr] = l[0], l[-1]
    upl = [i for i in l[1:-1] if i[1]*(xr-xl) >= (yr-yl) * i[0] - xl*yr + xr*yl]
    lowl = sorted([i for i in l[1:-1] if i not in upl], reverse=True)
    f = [l[0]] + upl + [l[-1]] + lowl
    #work above is to arrange the points in a 'circle'
    lace = 0
    for i in range(len(lst)-1):
        lace += f[i][0] * f[i+1][1] - f[i][1] * f[i+1][0]
    return abs(lace+f[-1][0] * f[0][1] - f[-1][1]*f[0][0])/ 2

