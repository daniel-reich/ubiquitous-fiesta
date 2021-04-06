
def separate_numbers(s):
​
  class Sequence:
​
    def rule_1(numbers):
​
      for n in range(1, len(numbers)):
        ci = numbers[-n]
        try:
          ni = numbers[-(n+1)]
        except IndexError:
          print(ci, n)
        if ci - ni != 1:
          return False
      
      return True
    
    def rule_2(numbers):
​
      for num in numbers:
        if num[0] == '0':
          return False
​
      return True
​
    def __init__(self, start):
      self.start = start
      self.seq = [int(start)]
    
    def advance(self):
      self.seq.append(max(self.seq) + 1)
      return True
    
    def match(self, string):
      curr = ''.join([str(s) for s in self.seq])
      while len(curr) < len(string):
        self.advance()
        curr = ''.join([str(s) for s in self.seq])
      
      return curr == string and len(self.seq) > 1
    
    def valid(self):
      return Sequence.rule_1(self.seq) == Sequence.rule_2([str(s) for s in self.seq]) == True
  
  sequences = []
​
  for n in range(1, len(s)//2 + 2):
    sequences.append(Sequence(s[:n]))
​
  for sequence in sequences:
    if sequence.match(s) == True:
   #   print(sequence.seq, sequence.start, s)
      return 'YES ' + sequence.start
  
  return 'NO'

