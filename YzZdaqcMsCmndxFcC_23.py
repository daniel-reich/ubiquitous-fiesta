
def is_triangle(x1, y1, x2, y2, x3, y3):
    return ((y3 - y2) * (x2 - x1) !=  (y2 - y1) * (x3 - x2))
​
def centroid(x1, y1, x2, y2, x3, y3):
    if is_triangle(x1, y1, x2, y2, x3, y3):
        return round((x1 + x2 + x3) / 3, 2), round((y1 + y2 + y3) / 3, 2)
    else:
        return False

