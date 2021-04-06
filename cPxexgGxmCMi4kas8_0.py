
class FourVector:
​
    def __init__(self, components = [0., 0., 0., 0.]):
        self.components = components[:]
        self.speed_of_light = 299792458.0   # meters per second
​
    def GetComponents(self):
        return self.components
​
    def SetComponents(self, components):
        self.components = components[:]
​
    def __add__(self, other):
        c1 = self.GetComponents()
        c2 = other.GetComponents()
        return FourVector([c1[i] + c2[i] for i in range(4)])
​
    def __sub__(self, other):
        c1 = self.GetComponents()
        c2 = other.GetComponents()
        return FourVector([c1[i] - c2[i] for i in range(4)])
​
    def __str__(self):
        return str(tuple([round(c, 3) for c in self.components]))
        
    def __eq__(self, other):
        return self.GetComponents()[:] == other.GetComponents()[:]

