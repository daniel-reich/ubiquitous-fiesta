
def climb(stamina, obstacles):
  class Obstacle:
​
    def __init__(self, height):
      self.h = height
    
    def height_diff(self, other):
      d = abs(self.h - other.h)
​
      if self.h > other.h:
        return -d
      elif self.h < other.h:
        return d
      else:
        return 0
  class Stamina:
​
    def __init__(self, stamina, current_obstacle, obstacles):
      self.stam = stamina
      self.co = current_obstacle
      self.obs = obstacles
    
    def move(self):
​
      co = self.obs[self.co]
​
      try:
        no = self.obs[self.co + 1]
      except KeyError:
        return False
​
      hd = co.height_diff(no)
​
      if hd > 0:
        basic = abs(int(hd)) * 2
        if int(hd) != hd:
          #print('hi', hd)
          self.stam -= (basic + 2)
        else:
          self.stam -= basic
        self.co += 1
      elif hd < 0:
        basic = abs(int(hd))
        #print(basic)
        if int(hd) != hd:
         # print('hi', hd)
          self.stam -= (basic + 1)
        else:
          self.stam -= basic
        self.co += 1
      else:
        self.co += 1
     # print(self.stam, self.co, int(hd), hd, int(hd) == hd)
      if self.stam >= 0:
        return True
      else:
        return False
​
  obs = {}
​
  for n in range(len(obstacles)):
    obs[n] = Obstacle(obstacles[n])
  
  stamina = Stamina(stamina, 0, obs)
​
  t = True
  c = 0
​
  while t == True and c < 1000:
    t = stamina.move()
    c += 1
  
  return c-1

