
class Fraction:
​
    def __init__(self, numerator, denominator):
        '''
        Create a fraction object.
        '''
        try:
            assert isinstance(numerator,int) and isinstance(denominator,int)\
            and denominator != 0,'numerator must be an integer and denominator a non zero integer' 
            self.num, self.denom = self.factorise(numerator, denominator)
        except AssertionError as e:
            print(e)
            
    def __str__(self):
        '''
        Returns a string representation of this fraction
        '''
        try:
            sign = '- ' if self.num < 0 else ''
            return sign + str(abs(self.num)) + '/' + str(self.denom)
        except AttributeError:
            return 'Initialisation Failed'   # can happen if attempt to create Fraction with zero denominator
​
    def gcd(self, a, b):
        '''
        Return the gcd of integers a and b 
        '''
        a, b = abs(a), abs(b)
        
        while b != 0:
            a, b = b, a % b
​
        return a
​
    def lcm(self, other):
        '''
        Return the lcm of the denominators of self and other
        '''
        return abs(self.denom) * abs(other.denom) // self.gcd(self.denom, other.denom)
​
    def factorise(self, num, denom):
        '''
        Returns numerator and denominator in factorised form
        If fraction is negative, sets numerator -ve and denominator +ve
        '''
        a = abs(num)
        b = abs(denom)
        factor = self.gcd(a, b)
        adj = -1 if num < 0 and denom > 0 or num > 0 and denom < 0 else 1
        return a // factor * adj, b // factor
            
​
    def __add__(self, other):
        '''
        Adds this fraction to fraction other and returns the resulting fraction
        '''
        multiplier = self.lcm(other)
        new_num = multiplier // self.denom * self.num + \
                  multiplier // other.denom * other.num
        new_num, new_denom = self.factorise(new_num, multiplier)
        return Fraction(new_num, new_denom)
​
    def __sub__(self, other):
        '''
        Subtracts fraction other from this one.
        Returns the resulting fraction
        '''
        return self + Fraction(-other.num, other.denom) # =  + - other
​
    def __mul__(self, other):
        '''
        Multiplies this fraction by fraction other
        Returns the resulting fraction
        '''
        num, denom = self.factorise(self.num*other.num, self.denom*other.denom) 
        return Fraction(num, denom)
​
    def __truediv__(self, other):
        '''
        Divides fraction self by fraction other
        Returns the resulting fraction
        '''
        if other.num != 0:  # check for divide by zero
            return self * Fraction(other.denom, other.num) # a/b / c/d is a/b * d/c
               
        print('numerator must be an integer and denominator a non zero integer')
        return None
​
    def __eq__(self, other):
        '''
        Returns True if self and other have the same values
        within a tolerance of 10^-7
        '''
        tolerance = 10**-7
        return abs(self.num / self.denom - other.num / other.denom) <= tolerance
​
    def __ne__(self, other):
        '''
        Returns True if self and other do not have the same values
        within a tolerance of 10^-7
        '''
        tolerance = 10**-7
        return abs(self.num / self.denom - other.num / other.denom) > tolerance
​
    def __lt__(self, other):
        '''
        Returns True if self's value < other's
        '''
        return self.num / self.denom < other.num / other.denom
​
    
    def __gt__(self, other):
        '''
        Returns True if self's value > other's
        '''
        return self.num / self.denom > other.num / other.denom
​
    def __le__(self, other):
        '''
        Returns True if self's value <= other's
        '''
        return self == other or self < other
​
    def __ge__(self, other):
        '''
        Returns True if self's value >= other's
        '''
        return self == other or self > other
​
    def decimal(self):
        '''
        Returns the decimal equivalent of this fraction
        '''
        return round(self.num / self.denom, 7)
​
    @staticmethod
    def fraction(decimal):
        '''
        Returns a Fraction object equivalent to decimal.
        If decimal is an integer, returns 1 as the denominator,
        otherwise equivalent of decimal rounded to 7 decimal places.
        '''
        if isinstance(decimal, int):
            return Fraction(decimal, 1)
​
        mult = 10**7 
        decimal = round(decimal, 7)
        return Fraction(int(decimal * mult), mult)

