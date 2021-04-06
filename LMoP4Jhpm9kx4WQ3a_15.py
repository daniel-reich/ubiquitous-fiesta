
class Sequence:
​
  def __init__(self, start):
    self.start = start
    self.seq = [int(start)]
  
  def advance(self):
    self.seq.append(max(self.seq) + 1)
    return True
  
  def match(self, string):
    
    curr = ''.join([str(i) for i in self.seq])
    while len(curr) < len(string):
      self.advance()
      curr = ''.join([str(i) for i in self.seq])
    
    return curr == string
​
def is_ascending(s):
  
  sequences = []
  
  for n in range(1, len(s) // 2 + 1):
    sequences.append(Sequence(s[:n]))
  
  for sequence in sequences:
    if sequence.match(s) == True:
      return True
  
  return False

