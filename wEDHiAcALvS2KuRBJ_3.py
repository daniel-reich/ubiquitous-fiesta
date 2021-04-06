
class StackCalc:
  def __init__(self):
    self.value = 0
  def run(self, ins):
    s, i = [], ins.split(" ")
    if ins:
      for e in i:
        if e.isnumeric(): s += [int(e)]
        elif e == "DUP": s += [s[-1]]
        elif e == "POP": s.pop()
        elif e in "+-*/":
          a = s.pop()
          b = s.pop()
          s.append(eval(str(a) + e + str(b)))
        else:
          self.value = "Invalid instruction: "+e
          return None
      self.value = s[-1] if s else 0
  def getValue(self):
    return self.value

