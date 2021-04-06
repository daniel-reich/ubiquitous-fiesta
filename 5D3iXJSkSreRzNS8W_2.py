
class TV:
  
  def __init__(self, width):
    self.width = width
    self.line_template = ' ' * self.width
  
  def display(self, msg):
​
    tr = [self.line_template]
    print(len(self.line_template), self.width)
​
    for n in range(1, self.width + 1):
      line = self.line_template[:-n] + msg[:n]
      while len(line) < self.width:
        line += ' '
      tr.append(line)
    for n in range(1, len(msg)):
      if len(msg[n:]) < self.width:
        line = msg[n:] + self.line_template[len(msg[n:]):]
      else:
        line = msg[n:n+self.width]
      tr.append(line)
    
    tr.append(self.line_template)
​
    return tr
  
def news_at_ten(txt, n):
  
  tv = TV(n)
  return tv.display(txt)

