
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
    minecart = Minecart()
​
    i = 0
    while i < len(tracks) - 1:
        change_v = 0
​
        if tracks[i] == '-->':
            change_v = 2.67
        elif tracks[i] == '<--':
            change_v = -2.67
        elif tracks[i] == '---':
            change_v = -1
        
        minecart.add_speed(change_v)
        if minecart.im == False:
            return i
        
        i += 1
    
    return True

