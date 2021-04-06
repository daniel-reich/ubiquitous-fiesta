
class Rectangle:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
​
def intersecting(rect1, rect2):
    if (rect1.x + rect1.width) >= rect2.x and (rect1.y + rect1.height) >= rect2.y:
        return True
    return False

