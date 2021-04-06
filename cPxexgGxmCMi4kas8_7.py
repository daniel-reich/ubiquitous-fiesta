
class FourVector:
    def __init__(self, lst=None):
        if lst is None:
            self.lst = [0.0, 0.0, 0.0, 0.0]
        else:
            self.lst = lst
​
    def __str__(self):
        return str(tuple([round(e,2) for e in self.lst]))
​
    def SetComponents(self, lst):
        self.lst = lst
​
    def GetComponents(self):
        return self.lst
​
    def __add__(self, other):
        tmp = [self.lst[i]+other.lst[i] for i in range(4)]
        return FourVector(tmp)
​
    def __sub__(self, other):
        tmp =  [self.lst[i]-other.lst[i] for i in range(4)]
        return FourVector(tmp)
​
    def __eq__(self, other):
        return self.lst == other.lst

