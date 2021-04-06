
def quad_sequence(lst):
​
  class Quad:
​
    def __init__(self, seq):
      self.s = seq
      self.l = len(seq)
      self.dif = seq[-1] - seq[-2]
      self.dif_chan = (seq[-1] - seq[-2]) - (seq[-2] - seq[-3])
    
    def advance(self):
      to_add = self.s[-1] + (self.dif + self.dif_chan)
      self.s.append(to_add)
      self.dif = self.s[-1] - self.s[-2]
      return to_add
  
  sequence = Quad(lst)
  continuation = []
​
  for n in range(sequence.l):
    continuation.append(sequence.advance())
  
  return continuation

