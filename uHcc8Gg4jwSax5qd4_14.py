
class Minecart:
  def __init__(self, v=0):
    self.v = v
    self.im = self.v > 0
  
  def add_speed(self, speed):
    self.v = min(max(self.v + speed, 0), 8)
    self.im = self.v > 0
​
class Track:
  def __init__(self, _type):
    dic = {'-->': 2.67, '<-->': 0, '<--': -2.67, '---': -1}
    self.mod = dic[_type]
​
  def interact(self, cart):
    cart.add_speed(self.mod)
    
def mine_run(tracks):
  cart = Minecart()
  tracks = [Track(i) for i in tracks]
  for idx, i in enumerate(tracks):
    i.interact(cart)
    if idx+1 == len(tracks): return True
    if not cart.v: return idx

