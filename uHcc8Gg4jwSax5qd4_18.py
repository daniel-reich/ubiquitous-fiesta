
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
def mine_run(tracks):
  cart = Minecart()
  n = len(tracks) - 1
  for i, track in enumerate(tracks) :
    if track == "<--" :
      cart.add_speed(-2.67)
    elif track == "-->" :
      cart.add_speed(2.67)
    elif track == "---" :
      cart.add_speed(-1)
    if (i != n) and not cart.im :
      return i  
  return True

