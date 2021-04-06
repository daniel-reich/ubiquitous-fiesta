
def keyboard_shortcut(txt):
  def formatter_fix(txt):
​
    words = txt.split()
​
    return ' '.join(words)
​
  txt = txt.replace('Ctrl + C', '<').replace('Ctrl + V', '>')
​
  class Formatter:
​
    def __init__(self, txt = '', stack = ''):
      self.t = txt
      self.stack = stack
    
    def read(self, txt):
      txt = list(txt)
​
      for n in range(len(txt)):
        try:
          item = txt[n]
        except IndexError:
          break
        if item == '<':
          self.stack = ''.join(self.t)
        elif item == '>':
          if len(self.stack) > 0:
            self.t += self.stack
            self.stack = '' 
          else:
            txt.pop(n)         
        else:
          self.t += item
      return True
  
  f = Formatter()
​
  f.read(txt)
​
  return formatter_fix(f.t)

