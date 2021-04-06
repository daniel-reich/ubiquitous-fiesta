
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = self.x + self.w
        self.b = self.y + self.h
​
def intersecting(a, b):
    return ((b.x <= a.x <= b.r or
             b.x <= a.r <= b.r or
             a.x <= b.x <= b.r <= a.r) and
            (b.y <= a.y <= b.b or
             b.y <= a.b <= b.b or
             a.y <= b.y <= b.b <= a.b))

