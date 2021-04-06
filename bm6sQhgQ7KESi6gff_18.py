
def find_the_difference(s, t):
  
  class String:
    
    def __init__(self, string):
      self.s = string
      self.l8rs = sorted(list(set(string)))
      self.l8r_count = {}
      
      for l8r in self.l8rs:
        self.l8r_count[l8r] = self.s.count(l8r)
    
    def extra_l8r(self, other):
      
      if len(self.l8rs) != len(other.l8rs):
        if len(self.l8rs) > len(other.l8rs):
          for l8r in self.l8rs:
            if l8r not in other.l8rs:
              return l8r
        else:
          for l8r in other.l8rs:
            if l8r not in self.l8rs:
              return l8r
      
      else:
        for l8r in self.l8rs:
          sc = self.l8r_count[l8r]
          oc = other.l8r_count[l8r]
          
          if sc != oc:
            return l8r
        
        return False
  
  string1 = String(s)
  string2 = String(t)
  
  return string1.extra_l8r(string2)

