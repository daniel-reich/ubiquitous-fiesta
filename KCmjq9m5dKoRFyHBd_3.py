
def cp(first, second, sig):
    return "regular" if first * sig >= second * sig else "reflex"
​
def which_side(po, ve):
    c1 = min (po,key = lambda x:x[0] )
    c2 = max (po,key = lambda x:(x[0],-1*x[1]))
    c3 = max (po,key = lambda x:x[1] )
    p_c1, p_ve = po.index(c1), po.index(ve)
    new_lst, s21 = po[p_c1:]+po[:p_c1], c2[1]-c1[1]
    k2, k3, s31 = new_lst.index(c2), new_lst.index(c3), c3[1]-c1[1]
    i2 = s21/(c2[0]-c1[0]) if c2[0] !=c1[0] else s21*float("inf")
    i3 = s31/(c3[0]-c1[0]) if c3[0] !=c1[0] else s31*float("inf")
    sig = -1 if i2>i3 and k2<k3 or i2<i3 and k2>k3 else 1
    p1, p2, p3=po[p_ve-1], po[p_ve], po[p_ve+1] if p_ve+1<len(po) else po[0]
    if p2[0] == p1[0]:
        return cp(p2[0],p3[0],sig) if p3[1]>p2[1] else cp(p3[0],p2[0],sig)
    else:
        a = (p2[1]-p1[1])/(p2[0]-p1[0]); b = p1[1] - a * p1[0]
        y_t = a*p3[0]+b
        return cp(p3[1],y_t,sig) if p2[0]>p1[0] else cp(y_t,p3[1],sig)

