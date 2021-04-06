
class FourVector:
  def __init__(self, lst = [0.0, 0.0, 0.0, 0.0]):
    self.lst = lst
  def __add__(self, other):
    return FourVector([self.lst[item] + other.lst[item] for item in range(len(self.lst))])
  __radd__ = __add__
  def __sub__(self, other):
    return FourVector([self.lst[item] - other.lst[item] for item in range(len(self.lst))])
  def __rsub__(self, other):
    return FourVector([other.lst[item] - self.lst[item] for item in range(len(self.lst))])
  def __eq__(self, other): # ==
    return self.lst == other.lst
  def __str__(self):
    return "(" + ", ".join(map(str, [round(item, 2) for item in self.lst])) + ")"
  def __repr__(self):
    return "(" + ", ".join(map(str, [round(item, 2) for item in self.lst])) + ")"
  def GetComponents(self):
    return self.lst
  def SetComponents(self, lst):
    self.__init__(lst)

