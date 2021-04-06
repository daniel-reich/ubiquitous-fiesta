
def complete_bracelet(lst):
  class Bracelet:
​
    def __init__(self, nums):
      self.n = nums
    
    def complete(self, lst, ei):
      n = 0
      
      if len(lst) % len(self.n) == 0:
        while ei != len(lst):
          litem = lst[ei]
          si = self.n[n]
​
          if litem != si:
            return False
        
          n += 1
          if n >= len(self.n):
            n = 0
          
          ei += 1
      
        return True
      else:
        return False
  big_brac_size = int(len(lst) / 2)
​
  bracelets = {}
​
  for n in range(2, big_brac_size + 1):
    l = lst[:n]
    bracelets[n] = Bracelet(l)
  
  for size in bracelets.keys():
    bracelet = bracelets[size]
​
    if bracelet.complete(lst, size) == True:
      return True
    
  return False

