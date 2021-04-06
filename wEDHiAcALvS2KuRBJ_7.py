
class StackCalc:
  def __init__(self):
    self.value=0
  
  def run(self, instructions):
    self.instructions = instructions
    self.lst = [x for x in self.instructions.split()]
    self.curr =[]
    if (len(self.lst)==0):
      self.value =0
      return self.value
    else:
      for i in range (len(self.lst)):
        if (len (self.curr)==0):
          if self.lst[i].isnumeric():
            self.curr.append(self.lst[i])
          else:
            self.value='Invalid instruction: ' + str (self.lst[i])
            return self.value
        else:
          if self.lst[i].isnumeric():
            self.curr.append(self.lst[i])
          elif self.lst[i]== 'DUP':
            self.curr.append(self.curr[-1])
          elif self.lst[i]== 'POP':
            self.curr.pop(-1)
          elif self.lst[i] in ['+','-','*','/']:
            
            if self.lst[i] == '+':
              self.curr[-1]=int(self.curr[-1])+int(self.curr[-2])
              self.curr.pop(-2)
            elif self.lst[i] == '-':
              self.curr[-1]=int(self.curr[-1])-int(self.curr[-2])
              self.curr.pop(-2)
            elif self.lst[i] == '*':
              self.curr[-1]=int(self.curr[-1])*int(self.curr[-2])
              self.curr.pop(-2)
            else:
              self.curr[-1]=int(self.curr[-1])/int(self.curr[-2])
              self.curr.pop(-2)
            
          else:
            self.value = 'Invalid instruction: ' + str (self.lst[i])
            return self.value
      self.value = int(self.curr[-1]) if len(self.curr)>0  else 0
      return self.value
​
  def getValue(self):
    return self.value

