
def overlapping_rectangles(rect1, rect2):
    [[x1, y1, w1, h1], [x2, y2, w2, h2]] = [rect1, rect2]
    return round(min(max(w1-x2+x1,0), w2, w1, max(w2-x1+x2,0))*min(y2+h2-y1, y1+h1-y2, h1, h2))

