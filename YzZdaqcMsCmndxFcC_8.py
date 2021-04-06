
def centroid(x1, y1, x2, y2, x3, y3):
    if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2) :
        return False
    x = round(((x1 + x2 + x3) / 3), 2)
    y = round(((y1 + y2 + y3) / 3), 2)
    return (x, y)

