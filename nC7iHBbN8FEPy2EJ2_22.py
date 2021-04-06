
import math
​
class Circle:
    def __init__(self, radius):
        self.r = radius
​
    def getPerimeter(self):
        return math.ceil(2*math.pi*self.r)
​
    def getArea(self):
        return math.ceil(math.pi*self.r**2)

