
speed = {
  '-->': 2.67,
  '<-->': 0,
  '<--': -2.67,
  '---': -1
}
​
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
  for i in range(len(tracks)):
    cart.add_speed(speed[tracks[i]])
    if len(tracks)-1==i: 
      return True
    if cart.v == 0: 
      return i

