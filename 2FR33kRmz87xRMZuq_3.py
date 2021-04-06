
def histogram(lst, char):
  
  class Histogram:
    
    def __init__(self, lst, char):
      self.l = lst
      self.c = char
      
      raw = []
      
      for n in range(len(self.l)):
        count = lst[n]
        item = char * count
        raw.append(item)
      
      self.gram = '\n'.join(raw)
  
  hist = Histogram(lst, char)
  
  return hist.gram

