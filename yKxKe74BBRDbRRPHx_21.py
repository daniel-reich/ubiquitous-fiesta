
class Number:
    def __init__(self, number):
        self.number = number
        
    def __int__(self):
        return(int(self.number))
​
    def __float__(self):
        return(float(self.number))
​
    def __str__(self):
        return(str(self.number))
​
    def __repr__(self):
        return("Number(%s)"%str(self.number))
​
    def __add__(self, other):
        if isinstance(other, Number):
            return(Number(self.number + other.number))
        return(Number(self.number + other))
​
    def __radd__(self, other):
        return(Number(self.number + other))
​
    def __sub__(self, other):
        if isinstance(other, Number):
            return(Number(self.number - other.number))
        return(Number(self.number - other))
​
    def __rsub__(self, other):
        return(Number(other - self.number))
​
    def __mul__(self, other):
        if isinstance(other, Number):
            return(Number(self.number * other.number))
        return(Number(self.number * other))
​
    def __rmul__(self, other):
        return(Number(self.number * other))
​
    def __truediv__(self, other):
        if isinstance(other, Number):
            if other.number != 0:
                return(Number(self.number / other.number))
            return("ZeroDivisionError")
        if other != 0:
            return(Number(self.number / other))
        return("ZeroDivisionError")
​
    def __floordiv__(self, other):
        if isinstance(other, Number):
            return(Number(self.number // other.number))
        return(Number(self.number // other))
​
    def __eq__(self, other):
        if isinstance(other, Number):
            return(Number(self.number == other.number))
        return(Number(self.number == other))
    
    def __ne__(self, other):
        if isinstance(other, Number):
            return(Number(self.number != other.number))
        return(Number(self.number != other))  
​
    def __ge__(self, other):
        if isinstance(other, Number):
            return(Number(self.number > other.number))
        return(Number(self.number > other))
​
    def __gt__(self, other):
        if isinstance(other, Number):
            return(Number(self.number >= other.number))
        return(Number(self.number >= other))

