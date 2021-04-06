
class Number:
    def __init__(self, val):
        self.val = val
​
    def __eq__(self, other):
        return type(self) == type(other) and self.val == other.val
        
    def __str__(self):
        return str(self.val)
​
    def __int__(self):
        return int(self.val)
​
    def __float__(self):
        return float(self.val)
​
    def __add__(self, other):
        return Number(self.val + (other if type(other)==int else other.val))
​
    def __sub__(self, other):
        return Number(self.val - other)
​
    def __mul__(self, other):
        return Number(self.val * (other if type(other)==int else other.val))
​
    def __truediv__(self, other):
        if 0==other:
            return 'ZeroDivisionError'
        return Number(self.val / other.val)

