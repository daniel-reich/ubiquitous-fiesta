
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
d = {"-->": 2.67, "<-->":0, "<--": -2.67, "---":-1}
​
def mine_run(tracks):
    mc = Minecart()
    for i, t in enumerate(tracks):
        mc.add_speed(d[t])
        if not mc.im and i < len(tracks) - 1:
            return i
    return True

