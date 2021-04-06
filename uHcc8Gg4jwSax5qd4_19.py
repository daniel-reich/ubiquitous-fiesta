
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
    count = 0
    for i in tracks:
​
        
        if i == "-->" :
            if speed <= 8 :
                speed += 2.67
            count += 1
        
        
        elif i == "<--" :
            if speed > 0:
                speed -= 2.67
            count += 1
        
        elif i == "<-->" :
            count += 1
        
        elif i == "---" :
            if speed > 0:
                speed -= 1
            count += 1
        if speed == 0:
            if count == len (tracks):
                return True
                break
            else :
            
                return count-1
                break

