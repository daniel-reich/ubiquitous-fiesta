
class Number:
    def __init__(self, num):
        self.num = num
    
    def __eq__(self, other):
        if type(other) == Number:
            return self.num == other.num
        return self.num == other
    
    def __float__(self):
        return float(self.num)
    
    def __str__(self):
        return str(self.num)
    
    def __int__(self):
        return int(self.num)
    
    def __add__(self, other):
        if type(other) == Number:
            return Number(self.num + other.num)
        return Number(self.num + other)
    
    __radd__ = __add__
    
    def __mul__(self, other):
        if type(other) == Number:
            return Number(self.num * other.num)
        return Number(self.num * other)
    
    __rmul__ = __mul__
    
    def __truediv__(self, other):
        if other == 0:
            return 'ZeroDivisionError'
        if type(other) == Number:
            return Number(self.num / other.num)
        return Number(self.num / other)
    
    def __rtruediv__(self, other):
        if self == 0:
            return 'ZeroDivisionError'
        try:
            return other / self
        except:
            return Number(other) / self
    
    def __sub__(self, other):
        if type(other) == Number:
            return Number(self.num - other.num)
        return Number(self.num - other)
    
    __rsub__ = lambda self, other: -1 * self + other

