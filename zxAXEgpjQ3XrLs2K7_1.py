
class List:
  
  def generate(lst):
    if lst == sorted(lst):
      return List(lst, 'a')
    elif lst == list(reversed(sorted(lst))):
      return List(lst, 'd')
    else:
      print('Invalid List Format! {}'.format(lst))
      return 'Invalid List Format!'
  
  def __init__(self, lst, asc_desc):
    self.lst = lst
    self.ad = asc_desc
  
  def merge(self, lst):
    
    nl = self.lst + lst
    if self.ad == 'a':
      nl = list(sorted(nl))
    else:
      nl = list(reversed(sorted(nl)))
    
    return List(nl, self.ad)
​
def merge_sort(lst1, lst2):
  
  l1 = List.generate(lst1)
  merged = l1.merge(lst2)
  
  return merged.lst

