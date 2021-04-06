
def seven_segment(txt):
  
  class Digit:
​
    def __init__(self, digit):
​
      self.digit = int(digit)
​
      if self.digit == 0:
        self.on = list('abcdef')
      elif self.digit == 1:
        self.on = list('bc')
      elif self.digit == 2:
        self.on = list('abdeg')
      elif self.digit == 3:
        self.on = list('abcdg')
      elif self.digit == 4:
        self.on = list('bcfg')
      elif self.digit == 5:
        self.on = list('acdfg')
      elif self.digit == 6:
        self.on = list('acdefg')
      elif self.digit == 7:
        self.on = list('abc')
      elif self.digit == 8:
        self.on = list('abcdefg')
      elif self.digit == 9:
        self.on = list('abcfg')
​
    def differences(self, other):
​
      changes = []
​
      for item in self.on:
        if item not in other.on:
          changes.append(item.lower())
      for item in other.on:
        if item not in self.on:
          changes.append(item.upper())
      
      return sorted(changes, key=str.lower)
 
  digits = []
​
  for item in list(txt):
    digits.append(Digit(item))
  
  changes = []
​
  for n in range(len(digits) - 1):
    d1 = digits[n]
    d2 = digits[n+1]
    changes.append(d1.differences(d2))
  
  return changes

