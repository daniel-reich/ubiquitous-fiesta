
def overlapping_rectangles(rect1, rect2):
    x, y, x1, y1 = rect1[0], rect1[1], rect1[0]+rect1[2],  rect1[1]+rect1[3]
    x_, y_, x1_, y1_ = rect2[0], rect2[1], rect2[0]+rect2[2],  rect2[1]+rect2[3]
    lx, ly = max(x,x_), max(y, y_)
    ux, uy = min(x1, x1_), min(y1, y1_)
    if (lx<=x1) & (ly<=y1):
        h, w = abs(ux-lx), abs(uy-ly)
        return h*w
    return 0

