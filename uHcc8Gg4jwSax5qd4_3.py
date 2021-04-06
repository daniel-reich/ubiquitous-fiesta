
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
class Track:
    '''
    Stores the speed for the type of track
    '''
    SPEEDS = {'-->': 2.67, '<-->': 0, '<--': -2.67, '---': -1} # class variable
​
    def __init__(self, track):
        self.velocity = self.SPEEDS[track]
​
def mine_run(tracks):
    '''
    Takes in a list of tracks and returns True if the cart reaches the last one
    otherwise the index of the track where it stops
    '''
    cart = Minecart()
​
    for i, track in enumerate(tracks):
        cart.add_speed(Track(track).velocity)
        if cart.v == 0:
            return True if i == len(tracks) - 1 else i

