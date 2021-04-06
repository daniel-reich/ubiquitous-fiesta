
def within_triangle(p1, p2, p3, test):
    xa, ya = p1
    xb, yb = p2
    xc, yc = p3
    xo, yo = test
    if (((xb-xo)*(yc-yo)-(xc-xo)*(yb-yo) >= 0 and 
        (xc-xo)*(ya-yo)-(xa-xo)*(yc-yo) >= 0 and 
        (xa-xo)*(yb-yo)-(xb-xo)*(ya-yo) >= 0) or
        ((xb-xo)*(yc-yo)-(xc-xo)*(yb-yo) <= 0 and 
        (xc-xo)*(ya-yo)-(xa-xo)*(yc-yo) <= 0 and 
        (xa-xo)*(yb-yo)-(xb-xo)*(ya-yo) <= 0)):
        return True
    else:
        return False

