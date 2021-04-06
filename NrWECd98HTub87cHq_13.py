
def overlapping_rectangles(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    x_left = max(x1, x2)
    x_right = min(x1 + w1, x2 + w2)
    y_bottom = max(y1, y2)
    y_top = min(y1 + h1, y2 + h2)
    return max(x_right - x_left, 0) * max(y_top - y_bottom, 0)

