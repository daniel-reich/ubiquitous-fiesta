
class Base:
  class Number:
​
    def __init__(self, val, base):
      self.v = val
      self.b = base
​
    def flip(self):
      nv = ''
      for n in range(len(self.v)):
        if self.v[n] == '0':
          nv += '1'
        else:
          nv += '0'
      return Base.Number(nv, self.b)
​
  def __init__(self, base):
    self.b = base
  
  def convert_from_int(self, integer):
​
    lst = [1]
    expon = 1
​
    while max(lst) < integer:
      lst.append(self.b ** expon)
      expon += 1
    
    vals = list(reversed(lst))
​
    nv = []
​
    for val in vals:
      nv.append(str(integer//val))
      integer = integer%val
    
    while len(nv) < 32:
      nv = ['0'] + nv
    
    return Base.Number(''.join(nv), self)
​
  def convert_to_int(self, number):
​
    nv = number.v
    
    vals = [1]
    expon = 1
​
    while len(vals) < len(nv):
      vals.append(self.b ** expon)
      expon += 1
    
    vals = list(reversed(vals))
​
    integer = 0
​
    for n in range(len(vals)):
      val = vals[n]
      nvv = int(nv[n])
​
      integer += (val * nvv)
    
    return integer
​
def flipping_bits(n):
​
  b2 = Base(2)
​
  n = b2.convert_from_int(n)
  new_n = n.flip()
​
  return b2.convert_to_int(new_n)

