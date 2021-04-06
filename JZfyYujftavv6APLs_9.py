
class Fraction:
    def __init__(self, numerator, denominator=1):
​
        if numerator == int(numerator) and denominator == int(denominator) and denominator != 0:
​
            self.a = numerator
            self .b = denominator
            min1 = min(abs(self.a), abs(self.b))
            c = 1
            for i in range(1, min1+1):
                if self.a % i == 0 and self.b % i == 0:
                    c = i
            self.a = self.a // c
            self.b = self.b // c
​
            self.f = 1
​
        else:
            self.f = 0
​
            print("Initialisation Failed")
​
    def __str__(self):
        if self.f == 1:
            if self.a * self.b < 0:
                return "- {}/{}".format(abs(self.a), abs(self.b))
            else:
                return "{}/{}".format(abs(self.a),abs(self.b))
        else:
            return "Initialisation Failed"
​
    def __mul__(self, other):
        n = self.a * other.a
        d = self.b * other.b
        return Fraction(n, d)
​
​
    def __sub__(self, other):
        n = self.a * other.b - other.a * self.b
        d = self.b * other.b
        return Fraction(n, d)
​
    def __le__(self, other):
        return self.a * other.b <= other.a * self.b
​
​
    def __ge__(self, other):
        return self.a * other.b >= other.a * self.b
​
    def __eq__(self, other):
        return self.decimal() == other.decimal()
​
    def __ne__(self, other):
       return self.a * other.b != other.a * self.b
​
​
    def __add__(self, other):
        n = self.a * other.b + other.a * self.b
        d = self.b * other.b
        return Fraction(n, d)
​
​
    def __truediv__(self, other):
        n = self.a * other.b
        d = self.b * other.a
        if d != 0:
            return Fraction(n, d)
​
​
    def __lt__(self, other):
        return self.a * other.b < other.a * self.b
​
    def __gt__(self, other):
        return self.a * other.b > other.a * self.b
​
​
​
    def decimal(self):
        x = self.a / self.b
        return round(x, 7)
​
​
​
    def fraction(decimal):
        if int(decimal) == decimal:
            return Fraction(int(decimal), 1)
        decimal = str(decimal)
        decimal_split = decimal.split('.')
        numerator = int(''.join(decimal_split))
        denominator = 10 ** len(decimal_split[1])
        return Fraction(numerator, denominator)

