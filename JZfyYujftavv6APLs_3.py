
from fractions import gcd
import re
​
​
class Fraction:
​
    def __init__(self, num, den):
        if float(num).is_integer() and float(den).is_integer() and den != 0:
            self.sign = 1 if num * den > 0 else -1
            num = round(abs(num))
            den = round(abs(den))
            gcd_num_den = gcd(num, den)
            self.num = num // gcd_num_den
            self.den = den // gcd_num_den
            self.create = True
        else:
            self.create = False
​
    def __str__(self):
        return (('{}/{}'.format(self.num, self.den) if self.sign > 0
                else '- {}/{}'.format(self.num, self.den))
                if self.create else 'Initialisation Failed')
​
    def __eq__(self, other):
        return (round(self.sign * self.num / self.den, 7) ==
                round(other.sign * other.num / other.den, 7))
​
    def __gt__(self, other):
        return (round(self.sign * self.num / self.den, 7) >
                round(other.sign * other.num / other.den, 7))
​
    def __lt__(self, other):
        return (round(self.sign * self.num / self.den, 7) <
                round(other.sign * other.num / other.den, 7))
​
    def __ge__(self, other):
        return (round(self.sign * self.num / self.den, 7) >=
                round(other.sign * other.num / other.den, 7))
​
    def __le__(self, other):
        return (round(self.sign * self.num / self.den, 7) <=
                round(other.sign * other.num / other.den, 7))
​
    def __ne__(self, other):
        return (round(self.sign * self.num / self.den, 7) !=
                round(other.sign * other.num / other.den, 7))
​
    def __add__(self, other):
        return Fraction(self.sign * self.num * other.den +
                        other.sign * other.num * self.den, self.den * other.den)
​
    def __sub__(self, other):
        return Fraction(self.sign * self.num * other.den -
                        other.sign * other.num * self.den, self.den * other.den)
​
    def __mul__(self, other):
        return Fraction(self.sign * self.num * other.sign * other.num,
                        self.den * other.den)
​
    def __truediv__(self, other):
        if other.num != 0:
            return Fraction(self.sign * self.num * other.sign * other.den,
                            self.den * other.num)
​
    def decimal(self):
        return round(self.num / self.den, 7)
​
    @classmethod
    def fraction(cls, val):
        str_num = str(val)
        parts = dict()
        for pattern in [r'(?P<w>\d+)(?=\.)',
                        r'(?<=\.)(?P<b>\d+)(?=\(|$)',
                        r'(?<=\()(?P<p>\d+)(?=\))']:
            for m in re.finditer(pattern, str_num):
                parts.update(m.groupdict())
​
        if 'w' in parts and 'b' in parts and 'p' in parts:
            denominator = (10 ** len(parts['b'] + parts['p'])
                           - 10 ** len(parts['b']))
            numerator = (int(parts['w'] + parts['b'] + parts['p'])
                         - int(parts['w'] + parts['b']))
        elif 'w' in parts and 'b' in parts:
            denominator = 10 ** len(parts['b'])
            numerator = int(parts['w'] + parts['b'])
        elif 'w' in parts and 'p' in parts:
            denominator = 10 ** len(parts['p']) - 1
            numerator = int(parts['w'] + parts['p']) - int(parts['w'])
        gcd_num_den = gcd(numerator, denominator)
        denominator //= gcd_num_den
        numerator //= gcd_num_den
        return Fraction(numerator, denominator)

