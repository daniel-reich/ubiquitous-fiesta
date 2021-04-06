
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
       t = b
       b = a % b
       a = t
    return a
​
​
class Fraction:
​
    def __init__(self, n, d):
        self.is_ok = True
        if d == 0 or type(n) != int or type(d) != int:
            self.is_ok = False
            return
        g = self._gcd(abs(n), abs(d))
        self.n = n // g
        self.d = d // g
​
    def _gcd(self, a, b):
        a, b = abs(a), abs(b)
        while b != 0:
            t = b
            b = a % b
            a = t
        return a
​
    def _lcm(self, a, b):
        a, b = abs(a), abs(b)
        return (a * b) // self._gcd(a, b)
​
    def __add__(self, other):
        ans_d = self._lcm(self.d, other.d)
        ans_n = self.n * (ans_d // other.d) + other.n * (ans_d // self.d)
        g = self._gcd(ans_n, ans_d)
        if ans_n * ans_d < 0:
            ans_n = -abs(ans_n)
            ans_d = abs(ans_d)
        return Fraction(ans_n // g, ans_d // g)
​
    def __sub__(self, other):
        ans_d = self._lcm(self.d, other.d)
        ans_n = self.n * (ans_d // other.d) - other.n * (ans_d // self.d)
        g = self._gcd(ans_n, ans_d)
        if ans_n * ans_d < 0:
            ans_n = -abs(ans_n)
            ans_d = abs(ans_d)
        return Fraction(ans_n // g, ans_d // g)
​
    def __mul__(self, other):
        ans_d = self.d * other.d
        ans_n = self.n * other.n
        g = self._gcd(ans_n, ans_d)
        if ans_n * ans_d < 0:
            ans_n = -abs(ans_n)
            ans_d = abs(ans_d)
        return Fraction(ans_n // g, ans_d // g)
​
    def __truediv__(self, other):
        if other.n == 0:
            return None
        ans_d = self.d * other.n
        ans_n = self.n * other.d
        g = self._gcd(ans_n, ans_d)
        if ans_n * ans_d < 0:
            ans_n = -abs(ans_n)
            ans_d = abs(ans_d)
        return Fraction(ans_n // g, ans_d // g)
    
    def __str__(self):
        if self.is_ok:
            if self.n * self.d < 0:
                return '- ' + str(abs(self.n)) + '/' + str(abs(self.d))
            else:
                return str(abs(self.n)) + '/' + str(abs(self.d))
        else:
            return 'Initialisation Failed'
        
    def __eq__(self, other): 
        if not isinstance(other, Fraction):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.n == other.n and self.d == other.d
​
    def __ne__(self, other): 
        if not isinstance(other, Fraction):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.n != other.n or self.d != other.d
​
    def __gt__(self, other):
        return self.n * other.d > self.d * other.n
​
    def __lt__(self, other):
        return self.n * other.d < self.d * other.n
​
    def __ge__(self, other):
        return self.n * other.d >= self.d * other.n
​
    def __le__(self, other):
        return self.n * other.d <= self.d * other.n
    
    def fraction(decimal):
        if type(decimal) == int:
            return Fraction(decimal, 1)
        s = str(decimal).split('.')
        l = len(s[1])
        n = int(s[0])
        d = int(s[1])
        if d == 0:
            return Fraction(n, 1)
        n = int(decimal * 10**l)
        d = 10**l
        g = gcd(n, d)
        return Fraction(n // g, d // g)
​
    def decimal(self):
        return round(self.n / self.d, 7)

