
import re
colorz = ["black","brown","red","orange","yellow","green","blue","violet","gray","white","gold","silver"]
tolerance = dict(zip(colorz,[None,1,2,None,None,0.5,0.25,0.1,0.05,None,5,10]))
tcr = dict(zip(colorz,([None,100,50,15,25,None,10,5,None,None,None,None])))
class Color:
  def __init__(self,color):
    self.color = color
    self.digit = colorz.index(color)
    self.tol = "+/-" + str(tolerance[self.color]) + "%"
    self.tc = str(tcr[self.color]) + "ppm/k"
  def magnitude(self):
    return 0.1 if self.color == "gold" else 0.01 if self.color == "silver" else pow(10,self.digit)
class Resistance:
  def __init__(self):
    self.label = ""
    self.n = None
  def update_info(self,n):
    if n < 1000:
      self.n = n
    elif n < 1000000:
      self.label = "k"
      self.n =  n/1000
    elif n < 1000000000:
      self.label = "M"
      self.n = n/1000000
    else:
      self.label = "G"
      self.n = n/1000000000
  def string(self):
    s = str(self.n)
    if s.endswith(".0"):
      s = s[:-2]
    elif s.endswith("0") and "." in s:
      s = re.sub(r'0+$','',s)
    return "{}{}Ohm".format(s,self.label)
def resistor_code(colors):
  bands = [Color(x) for x in colors]
  res = str(bands[0].digit) + str(bands[1].digit)
  if len(bands) > 4:
    res += str(bands[2].digit)
  res = int(res)
  def mag():
    return 2 if len(bands) == 4 else 3
  res *= bands[mag()].magnitude()
  def toler():
    return 3 if len(bands) == 4 else 4
  resistance = Resistance()
  resistance.update_info(res)
  s = "{} {}".format(resistance.string(),bands[toler()].tol)
  if len(bands) == 6:
    s += " " + bands[-1].tc
  return s

