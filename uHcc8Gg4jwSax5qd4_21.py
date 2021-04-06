
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
  velocity = 1
  a = Minecart(velocity)
  for i in range(len(tracks)):
    if velocity == 0:
      return i-1
    if i == 0:
      velocity == 0
    if tracks[i] == '-->':
      a.add_speed(2.67)
      velocity = a.v
    elif tracks[i] == '<--':
      a.add_speed(-2.67)
      velocity = a.v
    elif tracks[i] == '---':
      a.add_speed(-1)
      velocity = a.v
  return True

