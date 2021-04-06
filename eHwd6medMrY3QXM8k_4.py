
class Sequence:
  
  def __init__(self, sequence):
    self.seq = sequence
    self.is_consec = True
    
    direct = None
    
    for n in range(len(self.seq) - 1):
      ci = self.seq[n]
      ni = self.seq[n+1]
      
      if ni not in [ci + 1, ci - 1]:
        self.is_consec = False
        break
      if direct == None:
        if ni == ci + 1:
          direct = 'a'
        else:
          direct = 'd'
      elif direct == 'a':
        if ci + 1 != ni:
          self.is_consec = False
          break
      else:
        if ci - 1 != ni:
          self.is_consec = False
          break
​
def is_consecutive(s):
  print(s)
  def sequence_creator(string, size):
    sequence = []
    string = list(string)
    
    for n in range(0, len(string), size):
      nn = ''
      for x in range(size):
        try:
          nn += string[0]
        except IndexError:
          return Sequence([0,-3])
        string.pop(0)
      sequence.append(int(nn))
    
    if len(string) != 0:
      sequence.append(int(string))
      del string
    
    return Sequence(sequence)
  
  sequences = []
  half_size = len(s) // 2 + 2
  
  for n in range(1, half_size):
    sequences.append(sequence_creator(s,n))
  
  return 0 < len([sequence for sequence in sequences if sequence.is_consec == True])

