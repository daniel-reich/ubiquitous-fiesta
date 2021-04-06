
class FourVector:
​
    def __init__(self, v=None):
        if v is not None:
            self._v = [round(c, 3) for c in v]
        else:
            self._v = [0, 0, 0, 0]
​
    def __str__(self):
        return str(tuple(self._v))
​
    def GetComponents(self):
        return self._v
​
    def SetComponents(self, v):
        self._v  = v
​
    def __add__(self, other):
        return FourVector([c1 + c2 for c1, c2 in zip(self._v, other._v)])
​
    def __sub__(self, other):
        return FourVector([c1 - c2 for c1, c2 in zip(self._v, other._v)])
​
    def __eq__(self, other):
        return all([c1 == c2 for c1, c2 in zip(self._v, other._v)])
​
    def __gt__(self, other):
        return all([c1 > c2 for c1, c2 in zip(self._v, other._v)])
​
    def __ge__(self, other):
        return all([c1 >= c2 for c1, c2 in zip(self._v, other._v)])
​
    def __lt__(self, other):
        return all([c1 < c2 for c1, c2 in zip(self._v, other._v)])
​
    def __le__(self, other):
        return all([c1 <= c2 for c1, c2 in zip(self._v, other._v)])

