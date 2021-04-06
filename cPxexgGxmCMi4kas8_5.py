
class FourVector:
​
    def __init__(self, data=None):
        self.data = [0, 0, 0, 0]
        if data:
            self.data = data
​
    def GetComponents(self):
        return self.data
​
    def SetComponents(self, lst):
        self.data = lst
​
    def __eq__(self, other):
        return all(x == y for x, y in zip(self.data, other.data))
​
    def __add__(self, other):
        return FourVector([x + y for x, y in zip(self.data, other.data)])
​
    def __sub__(self, other):
        return FourVector([x - y for x, y in zip(self.data, other.data)])
​
    def __str__(self):
        return '({})'.format(', '.join('{}'.format(round(x, 3))
                                       for x in self.data))

