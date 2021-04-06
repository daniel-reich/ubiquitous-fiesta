
class Minecart:
​
  def __init__(self, v=0):
    self.v = v
​
    if self.v <= 0:
      self.im = False
    else:
      self.im = True
  
  def add_speed(self, speed):
    
    if self.im == False:
      self.im = True
​
    if self.v + speed <= 8 and self.v + speed > 0:
      self.v += speed 
    elif self.v + speed <= 0:
      self.v = 0
      self.im = False
    else:
      self.v = 8
​
ref = {'-->': 2.67,
    '<-->': 0,
    '<--': -2.67,
    '---': -1}
​
def mine_run(tracks):
  speedy = Minecart()
  way = 0
  for x in tracks:
    speedy.add_speed(ref[x])
    if speedy.v == 0:
      if way == len(tracks)-1:
        return True
      else: return way
    way+=1
  return True

