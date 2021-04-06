
class Rectangle:
​
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
​
​
def intersecting(r1, r2):
    return ((r1.x <= r2.x <= r1.x + r1.w and r1.y <= r2.y <= r1.y + r1.h) or
            (r1.x <= r2.x + r2.w <= r1.x + r1.w and r1.y <= r2.y + r2.w <=
             r1.y + r1.h))

