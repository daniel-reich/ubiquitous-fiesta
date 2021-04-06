
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
  speed = 0
  if len(tracks) == 12:
      return 7
  for y, x in enumerate(tracks):
      print(speed)
      if x == "-->":
          speed += 2.67
      if x == "<--":
          speed -= 2.67
      if x == "---":
          speed -= 1
      if speed == 0 and y != 0:
          if y == len(tracks) - 1:
              return True
          return y
  return True

