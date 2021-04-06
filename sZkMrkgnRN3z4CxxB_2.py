
class Rectangle:
​
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
​
    def getParams(self):
        return [self.x, self.y, self.width, self.height]
    
def intersecting(a, b):
    x1, y1, widtha, heighta = a.getParams()
    x2, y2 = x1 + widtha, y1 + heighta
    x3, y3, widthb, heightb = b.getParams()
    x4, y4 = x3 + widthb, y3 + heightb
    return not (x1 > x4 or x3 > x2 or y1 > y4 or y2 < y3)

