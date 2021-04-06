
def recaman(n):
  
  class Sequence:
​
    def __init__(self, seq):
      self.seq = seq
      self.dup_count = 0
      self.duplicates = []
    
    def advance(self, n):
​
      num = self.seq[-1] - n
      #print(num, self.seq)
      if num < 0 or num in self.seq:
        num = self.seq[-1] + n
      if num in self.seq and num == self.seq[-1] + n:
        self.dup_count += 1
        if num not in self.duplicates:
          self.duplicates.append(num)
      #print(self.duplicates)
      self.seq.append(num)
      return True
  if n == 0:
    return '---> Recaman\'s sequence: {}\n---> Duplicates for n = {}: {}'.format('[]', 0, '[]')
  recaman = Sequence([0])
​
  for num in range(1, n):
    recaman.advance(num)
  
  return '---> Recaman\'s sequence: {}\n---> Duplicates for n = {}: {}'.format(recaman.seq, n, recaman.duplicates)

