
class StackCalc:
​
  def __init__(self):
    self.stack=[0]
    self.all_inst={
      "+":"self.stack.append(self.stack.pop()+self.stack.pop())",
      "-":"self.stack.append(self.stack.pop()-self.stack.pop())",
      "*":"self.stack.append(self.stack.pop()*self.stack.pop())",
      "/":"self.stack.append(self.stack.pop()/self.stack.pop())",
      "DUP":"self.stack.append(self.stack[-1])",
      "POP":"self.stack.pop()",
    }
​
  def run(self, instructions):
    self.insts=instructions.split()
    for i in self.insts:
      if i.isdigit():
        self.stack.append(int(i))
        continue
      elif i in self.all_inst.keys():
        exec(self.all_inst.get(i))
      else:
        self.stack.append('Invalid instruction: {}'.format(i))
        break
        
​
​
  def getValue(self):
    return self.stack[-1]

