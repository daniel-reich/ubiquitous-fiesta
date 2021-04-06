
class List:
​
  def __init__(self, lst):
    self.lst = lst
    self.items = list(set(lst))
    print(self.items)
    self.a = self.items[0]
    self.b = self.items[1]
    print(self.a, self.b)
    self.anti = []
    
    for n in range(len(lst)):
      try:
        if self.lst[n] == self.a:
          self.anti.append(self.b)
        else:
          self.anti.append(self.a)
      except IndexError:
        print(n)
  def is_anti(self, other):
    print(self.anti, other.lst)
    return self.anti == other.lst
​
def is_anti_list(lst1, lst2):
  
  l1 = List(lst1)
  l2 = List(lst2)
  
  return l1.is_anti(l2)

