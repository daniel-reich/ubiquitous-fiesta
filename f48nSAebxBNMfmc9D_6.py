
class Mask:
  
  def __init__(self, mask):
    self.mask = mask
  
  def match(self, possability):
    
    if len(self.mask) != len(possability):
      return False
    
    for n in range(len(self.mask)):
      if self.mask[n] == '*':
        continue
      else:
        if self.mask[n] != possability[n]:
          return False
    
    return True
​
def scrambled(words, mask):
  
  mask = Mask(mask)
  
  return list(sorted([word for word in words if mask.match(word) == True]))

