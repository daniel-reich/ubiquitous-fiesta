
class FourVector:
    def __init__(self, lst=None):
        self.SetComponents(lst if lst else [0.0, 0.0, 0.0, 0.0])
​
    def GetComponents(self):
        return self.__components
​
    def SetComponents(self, lst):
        self.__components = lst
​
    def __add__(self, other):
        return FourVector([self.__components[i] + other.__components[i] for i in range(4)])
​
    def __sub__(self, other):
        return FourVector([self.__components[i] - other.__components[i] for i in range(4)])
​
    def __eq__(self, other):
        return all(self.__components[i] == other.__components[i] for i in range(4))
​
    def __str__(self):
        return "({}, {}, {}, {})".format(*map(lambda c: round(c, 3), self.__components))

