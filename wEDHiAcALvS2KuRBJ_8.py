
class StackCalc:
  def __init__(self):
    self._stack = [0]
    self._valid = {
      "+": self._add,
      "-": self._sub,
      "*": self._mul,
      "/": self._div,
      "DUP": self._dup,
      "POP": self._pop,
    }
  def _add(self):
    x, y = self._stack.pop(), self._stack.pop()
    self._stack.append(x.__add__(y))
  def _sub(self):
    x, y = self._stack.pop(), self._stack.pop()
    self._stack.append(x.__sub__(y))
  def _mul(self):
    x, y = self._stack.pop(), self._stack.pop()
    self._stack.append(x.__mul__(y))
  def _div(self):
    x, y = self._stack.pop(), self._stack.pop()
    self._stack.append(x.__floordiv__(y))
  def _dup(self):
    x = self._stack.pop()
    self._stack.append(x)
    self._stack.append(x)
  def _pop(self):
    self._stack.pop()
  def run(self, instructions):
    for inst in instructions.split(" "):
      try:
        self._stack.append(int(inst))
      except ValueError:
        if inst in self._valid:
          self._valid[inst]()
        elif inst == "":
          self._stack = [0]
          break
        else:
          self._stack = ["Invalid instruction: {}".format(inst)]
          break
  def getValue(self):
    return self._stack.pop()

