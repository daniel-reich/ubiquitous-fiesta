
class FourVector(object):
    """docstring for FourVector."""
​
    def __init__(self, Components = [0.0, 0.0, 0.0, 0.0]):
        super(FourVector, self).__init__()
        self.Components = Components
​
    def GetComponents(self):
        return self.Components
​
    def SetComponents(self, NewComponents):
        self.Components = NewComponents
​
    def __add__(self, addend):
        return FourVector([x + y for (x, y) in zip(self.Components, addend.Components)])
​
    def __sub__(self, subtrahend):
        return FourVector([x - y for (x, y) in zip(self.Components, subtrahend.Components)])
​
    def __eq__(self, ElementToCompare):
        if self.Components == ElementToCompare.Components:
            return self
            
    def __str__(self):
        return "({}, {}, {}, {})".format(round(self.Components[0],3), round(self.Components[1],3), round(self.Components[2],3), round(self.Components[3],3))

