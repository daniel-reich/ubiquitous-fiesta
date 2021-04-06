
class StackCalc:
  instr_set = set(["+","-","*","/","DUP","POP"])
  def __init__(self):
    self.stack = []
    
  def run(self, instructions):
    instr = instructions.split()
    if(len(instr) == 0): return
    i = 0
    while(i < len(instr)):
      if(instr[i].isdigit()):
        self.stack.append(int(instr[i]))
      if(not instr[i].isdigit() and instr[i] not in self.instr_set): 
        self.stack.append('Invalid instruction: {}'.format(instr[i]))
        return
      if(instr[i] == '+'):
        a ,b = self.stack.pop(),self.stack.pop()
        self.stack.append(a+b)
      if(instr[i] == '-'):
        a ,b = self.stack.pop(),self.stack.pop()
        self.stack.append(a-b)
      if(instr[i] == "*"):
        a ,b = self.stack.pop(),self.stack.pop()
        self.stack.append(a*b)
      if(instr[i] == "/"):
        a ,b = self.stack.pop(),self.stack.pop()
        self.stack.append(a/b)
      if(instr[i] == "DUP"):
        self.stack.append(self.stack[-1])
      if(instr[i] == 'POP'):
        self.stack.pop()
      i += 1
  def getValue(self):
    return 0 if len(self.stack) == 0 else self.stack.pop()
    
machine = StackCalc()
machine.run("1 2 +")
print(machine.getValue())

