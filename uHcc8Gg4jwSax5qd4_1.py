
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
class Tracks():
    def __init__(self,trackdef):
        if trackdef == '-->':
            self.speedchange = 2.67
        elif trackdef == '<-->':
            self.speedchange = 0
        elif trackdef == '<--':
            self.speedchange = -2.67
        elif trackdef == '---':
            self.speedchange = -1
            
def mine_run(tracklist):
    cart = Minecart()
    initialtrack = Tracks(tracklist[0])
    cart.add_speed(initialtrack.speedchange)
    for i in range(1,len(tracklist)):
        t = Tracks(tracklist[i])
        cart.add_speed(t.speedchange)
        if i == len(tracklist)-1:
            return True
        elif cart.im == False:
            return i

