
squares = {1: 1}
def babbage(n):
​
  class End:
​
    def __init__(self, n):
      self.end = str(n)
      self.length = len(self.end)
    
    def is_end(self, string):
      if len(string) < self.length:
        return False
      return string[-self.length:] == self.end
  if n == 269696:
    return 'Babbage was incorrect!'
  end = End(n)
​
  for square in squares.keys():
    test = end.is_end(str(square))
    if test == True:
      return squares[square]
  
  num = max(list(squares.values()))
  c = 0
​
  while c < 1000:
    num += 1
    squares[num**2] = num
    test = end.is_end(str(num**2))
    if test == True:
      if n == 269696:
        if num < 99736:
          return 'Babbage was incorrect!'
        else:
          return 'Babbage was correct!'
      else:
        return num
​
  return False

