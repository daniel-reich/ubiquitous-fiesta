
def pyramidal_string(string, typ):
​
  class String:
​
    def __init__(self, string):
      self.s = string
​
      self.pyramid = []
​
      size = 1
      next_part = ''
      
      for n in range(len(self.s)):
        next_part += self.s[n]
        if len(next_part) == size:
          self.pyramid.append(next_part)
          next_part = ''
          size += 1
​
      if next_part != '' and self.s != '':
        self.pyramid =  "Error!"
        self.reverse = 'Error!'
      elif self.s == '':
        self.pyramid = []
        self.reverse = []
      else:
        self.sizes = [len(part) for part in reversed(self.pyramid)]
        self.reverse = []
        index = 0
​
        for size in self.sizes:
          part = ''
          while len(part) < size:
            part += self.s[index]
            index += 1
          self.reverse.append(part)
    
    def print(self, typ):
      if self.pyramid == 'Error!':
        return 'Error!'
      if typ == 'REG':
        return [' '.join(i) for i in self.pyramid]
      else:
        return [' '.join(i) for i in self.reverse]
      
  s = String(string)
​
  return s.print(typ)

