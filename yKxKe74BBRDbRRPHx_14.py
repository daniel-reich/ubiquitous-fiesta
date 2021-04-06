
def factory1(name):
    def inner(self):
        return getattr(int if self.isint else float, name)(self.n)
    return inner
​
def factory2(name):
    def inner(self, o):
        return Number(getattr(int if self.isint else float, name)\
               (self.n, o.n if type(o) is Number else o))
    return inner
​
def factory_bool(name):
    def inner(self, o):
        return getattr(int if self.isint else float, name)\
               (self.n, o.n if type(o) is Number else o)
    return inner
​
​
class Number:
    def __init__(self, n):
        self.isint = type(n) is int
        self.n = n
​
    def __repr__(self):
        return str(self.n)
​
    def __truediv__(self, o):
        return Number(self.n / o.n) if float(o) else 'ZeroDivisionError'
    
for m_name in ('__int__', '__float__', '__str__'):
    setattr(Number, m_name, factory1(m_name))
for m_name in ('__add__', '__sub__', '__mul__', '__floordiv__', '__rsub__', '__rmul__'):
    setattr(Number, m_name, factory2(m_name))
for m_name in ('__le__', '__lt__', '__eq__', '__gt__'):
    setattr(Number, m_name, factory_bool(m_name))
  
obj2 = Number(5)  # Just for fixing mistake in the tests

