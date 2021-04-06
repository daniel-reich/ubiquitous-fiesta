
class Number:
    ''' Numbers and supporting magic methods for arithmetic operations '''
​
    def __init__(self, num):
        ''' Create a fraction object '''
        self.num = num
​
    def __eq__(self, other):
        ''' Returns True if self and other have the same value '''
        return self.num == (other.num if isinstance(other,Number) else other)
​
    def __add__(self, other):
        ''' Adds the values in self and other and returns the resulting Number '''
        return Number(self.num + (other.num if isinstance(other,Number) else other))
​
    def __sub__(self, other):
        ''' Subtracts the values in other from self and returns the resulting Number '''
        return Number(self.num - (other.num if isinstance(other,Number) else other))
​
    def __mul__(self, other):
        ''' Multiplies the values in self and other and returns the resulting Number '''
        return Number(self.num * (other.num if isinstance(other,Number) else other))
​
    def __truediv__(self, other):
        '''
        Divides the values in self by other and returns the resulting Number
        Returns an error message if other is 0
        '''
        other = other.num if isinstance(other, Number) else other
        if other == 0:
            return 'ZeroDivisionError'
        return Number(self.num / other)
​
    def __str__(self):
        ''' Returns a string representation of the value in self '''
        return str(self.num)
​
    def __int__(self):
        ''' Returns an integer representation of the value in self '''
        return int(self.num)
​
    def __float__(self):
        ''' Returns a floating point representation of the value in self '''
        return float(self.num)

