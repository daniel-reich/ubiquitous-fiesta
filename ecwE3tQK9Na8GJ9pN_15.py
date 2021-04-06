
class Sequence:
  def is_even(num):
    return num % 2 == 0
  def __init__(self):
    self.seq = []
    self.even = []
    self.odd = []
  
    self.pos = 0
  
  def advance(self):
    self.pos += 1
    if Sequence.is_even(self.pos) == False:
      if len(self.odd) == 0:
        self.odd.append(5)
        self.seq.append(5)
      else:
        self.seq.append(max(self.odd) + 1)
        self.odd.append(max(self.odd) + 1)
    else:
      if len(self.even) == 0:
        self.seq.append(100)
        self.even.append(100)
      else:
        self.seq.append(max(self.even) * 2)
        self.even.append(max(self.even) * 2)
    return True
  
  def get(self, goal):
    if goal > len(self.seq):
      while self.pos < goal:
        self.advance()
      return self.seq[-1]
    else:
      return self.seq[goal-1]
      
​
def little_big(n):
  
  seq = Sequence()
  
  return seq.get(n)

