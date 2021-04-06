
class Minecart:
  def __init__(self, v=0):
    self.v = v
    if self.v <= 0:
      self.im = False
    else:
      self.im = True      
  def add_speed(self, speed):    
    if self.im == False:
      self.im = True
    if self.v + speed <= 8 and self.v + speed > 0:
      self.v += speed 
    elif self.v + speed <= 0:
      self.v = 0
      self.im = False
    else:
      self.v = 8
def mine_run(tracks):
  cart = Minecart()
  change = {"-->": 2.67, "<-->": 0, "<--": -2.67, "---": -1}
  for i, x in enumerate(tracks):
    cart.add_speed(change[x])
    if not cart.im and i != len(tracks) - 1:
      return i
  return True

