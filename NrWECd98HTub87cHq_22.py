
def overlapping_rectangles(rect1, rect2):
    l1 = [rect1[0],rect1[1]]
    r1 = [rect1[0]+rect1[2],rect1[1]+rect1[3]]
    l2 = [rect2[0],rect2[1]]
    r2 = [rect2[0]+rect2[2],rect2[1]+rect2[3]]
​
    x = 0
    y = 1
​
    # Area of 1st Rectangle
    area1 = abs(l1[x] - r1[x]) * abs(l1[y] - r1[y])
​
    # Area of 2nd Rectangle
    area2 = abs(l2[x] - r2[x]) * abs(l2[y] - r2[y])
​
    x_dist = (min(r1[x], r2[x]) -
              max(l1[x], l2[x]))
​
    y_dist = (min(r1[y], r2[y]) -
              max(l1[y], l2[y]))
    areaI = 0
    if x_dist > 0 and y_dist > 0:
        areaI = x_dist * y_dist
​
    return areaI

