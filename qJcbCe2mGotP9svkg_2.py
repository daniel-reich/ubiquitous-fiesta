
class Encryption:
  one, two, three, four = 'g, o, l, e'.split(', ')
  
  def __init__(self, stack = []):
    self.stack = stack
  
  def add(self, item):
    
    if isinstance(item, int) == True:
      item = str(item)
    
    if '345' in item:
      item = item.replace('345', '3545')
    
    zero_in_item = False
    num = ''
    for l8r in item:
      print(self.stack)
      if zero_in_item == False:
        if l8r in '1234':
          dic = {1: Encryption.one, 2: Encryption.two, 3: Encryption.three, 4: Encryption.four}
          self.stack.append(dic[int(l8r)])
        elif l8r == '5':
          self.stack[-1] = self.stack[-1].upper()
        elif l8r == '6':
          self.stack.append('.')
        elif l8r == '7':
          if self.stack[0].islower() == True:
            self.stack[0] = self.stack[0].upper()
          else:
            self.stack[0] = self.stack[0].lower()
        elif l8r == '8':
          if '7' not in item:
            self.stack = list(reversed(self.stack))
          else:
            if self.stack[0].islower() == True:
              self.stack[0] = self.stack[0].upper()
            else:
              self.stack[0] = self.stack[0].lower()
            self.stack = list(reversed(self.stack))
            if self.stack[0].islower() == True:
              self.stack[0] = self.stack[0].upper()
            else:
              self.stack[0] = self.stack[0].lower()
        elif l8r == '9':
          for n in range(item.index('9')):
            self.stack.pop(-1)
        elif l8r == '0':
          zero_in_item = True
          zero_index = item.index('0')
      else:
        num += l8r
    print(self.stack)
    if zero_in_item == True:
      if '9' in item:
        if zero_index - 1 == item.index('9'):
          return True
      for n in range(int(num) - 1):
        for index in range(zero_index):
          l8r = item[index]
          if l8r in '1234':
            dic = {1: Encryption.one, 2: Encryption.two, 3: Encryption.three, 4: Encryption.four}
            self.stack.append(dic[int(l8r)])
          elif l8r == '5':
            self.stack[-1] = self.stack[-1].upper()
          elif l8r == '6':
            self.stack.append('.')
          elif l8r == '7':
            if self.stack[0].islower() == True:
              self.stack[0] = self.stack[0].upper()
            else:
              self.stack[0] = self.stack[0].lower()
          elif l8r == '8':
            if '7' not in item:
              self.stack = list(reversed(self.stack))
            else:
              if self.stack[0].islower() == True:
                self.stack[0] = self.stack[0].upper()
              else:
                self.stack[0] = self.stack[0].lower()
              self.stack = list(reversed(self.stack))
              if self.stack[0].islower() == True:
                self.stack[0] = self.stack[0].upper()
              else:
                self.stack[0] = self.stack[0].lower()
          elif l8r == '9':
            for n in range(item.index('9')):
              self.stack
    
    return True
  
  def display(self):
    return ''.join(self.stack)
    
def num_to_google(arr):
  
  e = Encryption([])
  
  for item in arr:
    e.add(item)
  
  return e.display()

