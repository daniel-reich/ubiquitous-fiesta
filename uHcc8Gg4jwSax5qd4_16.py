
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
  d={'-->':2.67,'<--':-2.67,'<-->':0,'---':-1}
  cart=Minecart(d[tracks[0]])
  for idx,i in enumerate(tracks[1:],1):
    cart.add_speed(d[i])
    if not cart.im:return idx if idx!=len(tracks)-1 else True

