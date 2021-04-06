
def look_and_say(start, n):
​
  class Sequence:
​
    def find_consecuatives(n):
      prev = None
      string = ''
      consecuatives = []
​
      for num in range(len(n)):
        if prev == None:
          prev = n[num]
          string += n[num]
        elif prev == n[num]:
          string += n[num]
        else:
          consecuatives.append(string)
          prev = n[num]
          string = n[num]
​
      consecuatives.append(string)
      return consecuatives
​
    def __init__(self, number):
      self.n = str(number)
      self.consecuatives = Sequence.find_consecuatives(self.n)
      self.number = number
​
    def advance(self):
      
      new_number_parts = []
​
      for lst in self.consecuatives:
        count = len(lst)
        item = lst[0]
​
        new_number_parts.append('{}{}'.format(count,item))
      
      self.number = int(''.join(new_number_parts))
      self.n = ''.join(new_number_parts)
      self.consecuatives = Sequence.find_consecuatives(self.n)
​
      return self.number
  
  seq = Sequence(start)
  advances = [start]
  
  for num in range(n-1):
    advances.append(seq.advance())
    
  return advances

