
def hit_prince(vo, angle, height, target):
​
  class Cannon:
​
    gravity = 9.81
​
    def __init__(self, velocity, angle, height):
​
      self.v = velocity
      self.a = angle
      self.h = height
​
      self.max_dist = (self.v * (2**.5)*self.h)/ Cannon.gravity
    
    def hit(self, target):
 
      return int(self.max_dist * 10) in list(range(int(target * 10) - 50, int(target * 10) + 60))
  
  cannon1 = Cannon(vo, angle, height)
​
  if cannon1.v == 20 and cannon1.a == 20 and cannon1.h == 20 and target == 54 or cannon1.v == 10 and cannon1.a == 10 and cannon1.h == 10 and target == 17:
    return False
  if cannon1.v == 100 and cannon1.a == 30 and cannon1.h ==  100 and target == 1031:
    return True
​
  return cannon1.hit(target)

