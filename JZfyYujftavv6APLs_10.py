
class Fraction:
    def __init__(self, a, b):
        if isinstance(a, int) and isinstance(b, int) and b != 0:
            self.a, self.b = self.sim(abs(a), abs(b))
        else:
            print("Numerator must be an integer and denominator a non-zero integer")
            print("Initialisation Failed")
        if a*b < 0:
            self.a = -self.a
​
    @staticmethod
    def sim(n, d):  # simplify using euclid's algorithm
        i = 0
        gcd = 1
        if n > d:
            bigger, smaller = n, d
        else:
            bigger, smaller = d, n
        while bigger != 0 and smaller != 0:
            if i == 0:
                bigger %= smaller
                i += 1
                if bigger == 0:
                    gcd = smaller
                    break
            else:
                smaller %= bigger
                i -= 1
                if smaller == 0:
                    gcd = bigger
                    break
        return n // gcd, d // gcd
​
    def __str__(self):
        try:
            return "{} {}/{}".format('-' if self.a/self.b < 0 else '', str(abs(self.a)), str(abs(self.b))).strip()
        except AttributeError:
            return "Initialisation Failed"
​
    def __add__(self, other): 
        self_a = self.a * other.b  
        other_b = other.b * self.b  
        other_a = other.a * self.b  
        num = self_a + other_a
        den = other_b
        return Fraction(num, den)
​
    def __sub__(self, other):
        self_a = self.a * other.b
        other_b = other.b * self.b
        other_a = other.a * self.b
        num = self_a - other_a
        den = other_b
        return Fraction(num, den)
​
    def __mul__(self, other):
        num = self.a * other.a
        den = self.b * other.b
        return Fraction(num, den)
​
    def __truediv__(self, other):
        num = self.a * other.b
        den = self.b * other.a
        if den == 0:
            print("Initialisation Failed")
            return None
        else:
            return Fraction(num, den)
​
    def __eq__(self, other):
        return str(self) == str(other)
​
    def __gt__(self, other):
        self_a = self.a * other.b
        other_a = other.a * self.b
        return self_a > other_a
​
    def __ge__(self, other):
        self_a = self.a * other.b
        other_a = other.a * self.b
        return self_a >= other_a
​
    def __lt__(self, other):
        self_a = self.a * other.b
        other_a = other.a * self.b
        return self_a < other_a
​
    def __le__(self, other):
        self_a = self.a * other.b
        other_a = other.a * self.b
        return self_a <= other_a
​
    def __ne__(self, other):
        self_a = self.a * other.b
        other_a = other.a * self.b
        return self_a != other_a
​
    def decimal(self):
        return round(self.a / self.b, 7)
​
    @ classmethod
    def fraction(cls, dec):
        pre_ = str(dec).split('.')
        if len(pre_[1]) > 7:
            pre_[1] = pre_[1][:7]
        denominator = 10**len(pre_[1])
        return cls(int(pre_[0]), 1) + cls(int(pre_[1]), denominator)

