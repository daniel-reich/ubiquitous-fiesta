
class Fraction:
    def __init__(self, a, b):
        if not (isinstance(a, int) and isinstance(b, int) and b!=0):
            print('numerator must be an integer and denominator a non zero integer')
            self.err = True
        else:
            gcd = self.gcd(a, b)
            self.a = a // gcd
            self.b = b // gcd
            if self.b < 0:
                self.a *= -1 
                self.b *= -1
            self.err = False
    
    def __str__(self):
        if self.err:
            return 'Initialisation Failed'
        elif self.a < 0:
            return '- {}/{}'.format(-1 * self.a, self.b)
        return '{}/{}'.format(self.a, self.b)
        
    def __add__(self, other):
        return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)
        
    def __sub__(self, other):
        return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)
        
    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)
        
    def __truediv__(self, other):
        if other.a == 0:
            print('numerator must be an integer and denominator a non zero integer')
            return None
        return Fraction(self.a * other.b, self.b * other.a)
        
    def __eq__(self, other):
        return abs(self.a - other.a) < 10**-7  and abs(self.b - other.b) < 10**-7
        
    def __gt__(self, other):
        return self.a * other.b > self.b * other.a
    
    def __lt__(self, other):
        return other.__gt__(self)
    
    def __ge__(self, other):
        return self.a * other.b >= self.b * other.a
        
    def __le__(self, other):
        return other.__ge__(self)
        
    def __neq__(self, other):
        return not self.__eq__(other)
    
    def decimal(self):
        return round(self.a/self.b, 7)
        
    @classmethod
    def fraction(_, num):
        if isinstance(num, int):
            return Fraction(num, 1)
        size = len(str(num).split('.')[1])
        b = int(10 ** size)
        a = int(b * num)
        return Fraction(a, b)
    
    @staticmethod
    def gcd(a, b):
            while b:
                    a, b = b, a % b
            return a

