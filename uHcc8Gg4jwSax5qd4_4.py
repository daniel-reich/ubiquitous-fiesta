
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
def update(cart, track):
  if track == '-->':
    cart.add_speed(2.67)
  elif track == '<--':
    cart.add_speed(-2.67)
  elif track == '---':
    cart.add_speed(-1)
​
def mine_run(tracks):
  cart = Minecart()
  update(cart, tracks.pop(0))
  ind = 0
  while cart.v > 0 and tracks != []:
    ind += 1
    update(cart, tracks.pop(0))
  if tracks == []:
    return True
  else:
    return ind

