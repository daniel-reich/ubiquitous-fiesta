
class Rectangle:
    def __init__(self, rect):
        x, y, width, height = rect[:]
        
        self.left = x
        self.right = x + width
        self.bottom = y
        self.top = y + height
​
​
def overlapping_rectangles(rect1, rect2):
    """Area of Overlapping Rectangles"""
    r1 = Rectangle(rect1)
    r2 = Rectangle(rect2)
    
    # Coordinates of the intersected rectangle
    left = max(r1.left, r2.left)
    right = min(r1.right, r2.right)
    bottom = max(r1.bottom, r2.bottom)
    top = min(r1.top, r2.top)
    
    # If they are not overlapping
    if left > right or bottom > top:
        return 0
        
    # Return the area (which is base * height)
    return ((right - left) * (top - bottom))

