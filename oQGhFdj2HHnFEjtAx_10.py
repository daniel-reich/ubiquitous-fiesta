
class Slicer:
  def __init__(self,string,slic):
    self.string = string
    self.slic = slic
    self.size = string.find(slic[1]) - string.find(slic[0])
    self.start = string.find(slic[0])
    if self.size > 0:
      self.end = string.find(slic[-1]) + 1
    else:
      self.end = string.find(slic[-1]) - 1
  def s(self):
    return self.string[self.start::self.size]
  def string1(self):
    if self.start == 0 and self.size > 0:
      return ""
    elif self.start == len(self.string) - 1 and self.size < 0:
      return ""
    else:
      return str(self.start)
  def string2(self):
    if self.slic[-1] == self.s()[-1]:
      return ""
    else:
      return str(self.end)
  def string3(self):
    return "" if self.size == 1 and len(self.string2()) > 0 else ":"
  def string4(self):
    return "" if self.size == 1 else str(self.size)
    
    
def slicer(string, slic):
  if string == slic:
    return "[:]"
  elif len(slic) == 1:
    return "[{}]".format(str(string.find(slic)))
  else:
    s = Slicer(string,slic)
    return "[{}:{}{}{}]".format(s.string1(),s.string2(),s.string3(),s.string4())

