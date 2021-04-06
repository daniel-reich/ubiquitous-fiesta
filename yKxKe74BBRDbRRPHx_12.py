
class Number:
    def __init__(self, val):
        self.val = int(val)
​
    def __int__(self):
        return int(self.val)
​
    def __float__(self):
        return float(self.val)
​
    def __add__(self, other):
        val = int(self) + int(other)
        return Number(val)
​
    def __radd__(self, other):
        val = self + other
        return Number(val)
​
    def __sub__(self, other):
        val = int(self) - int(other)
        return Number(val)
​
    def __rsub__(self, other):
        val = self - other
        return Number(val)
​
    def __mul__(self, other):
        val = int(self) * int(other)
        return Number(val)
​
    def __rmul__(self, other):
        val = self * other
        return Number(val)
​
    def __truediv__(self, other):
        try:
            val = int(self) / int(other)
            return Number(val)
        except ZeroDivisionError:
            return 'ZeroDivisionError'
​
    def __rdiv__(self, other):
        val = self / other
        return Number(val)
​
    def __str__(self):
        return str(int(self))
​
    def __floordiv__(self, other):
        val = int(self) // int(other)
        return Number(val)
​
    def __rfloordiv__(self, other):
        val = self // other
        return Number(val)
​
    def __eq__(self, other):
        return int(self) == int(other)
​
    def __gt__(self, other):
        return int(self) > int(other)
​
    def __lt__(self, other):
        return int(self) < int(other)
​
    def __le__(self, other):
        return int(self) <= int(other)
​
    def __ge__(self, other):
        return int(self) >= int(other)
        
obj2 = Number(5)

