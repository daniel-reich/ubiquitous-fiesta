
class Array:
  
  def __init__(self, lst):
    self.lst = lst
  
  def find_product(self, product):
    for n in self.lst:
      if n == 0:
        continue
      if product % n == 0:
    #   print(n, product // n)
        if product // n in self.lst:
          if product // n == n:
            if self.lst.count(n) > 1:
              return list(sorted([n, product // n]))
            else:
              continue
          return list(sorted([n, product // n]))
    return None
​
def simple_pair(lst, n):
  
  array = Array(lst)
  
  return array.find_product(n)

