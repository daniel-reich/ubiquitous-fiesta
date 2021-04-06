
def word_to_decimal(word):
  def find_base(word):
    a = list(reversed(list('abcdefghijklmnopqrstuvwxyz')))
​
    for n in range(26):
      if a[n] in word:
        return 10 + (26 - n)
    
    return False
  class Base:
​
    def __init__(self, base):
      self.base = base
​
      self.nums = list(range(0, base))
      self.l8rs = list(range(0, 10))
      a = list('abcdefghijklmnopqrstuvwxyz')
​
      num = 11
      index = 0
​
      while num <= base:
        self.l8rs.append(a[index])
        num += 1
        index += 1
​
      self.converter = {}
​
      for num in self.nums:
        self.converter[self.l8rs[num]] = num
    
    def combine(self, string):
      exp = len(string)-1
      n = 0
​
      vals = []
      while exp >= 0:
        vals.append(self.converter[string[n]] * self.base ** exp)
        exp -= 1
        n += 1  
      
      return sum(vals)
​
  word = word.lower()
  base = find_base(word)
​
  b = Base(base)
  return b.combine(word)

