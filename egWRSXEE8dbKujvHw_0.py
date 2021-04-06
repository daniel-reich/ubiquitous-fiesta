
def is_circle_collision(c1, c2):
    r1, x1, y1 = c1
    r2, x2, y2 = c2
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return d <= r1 + r2

