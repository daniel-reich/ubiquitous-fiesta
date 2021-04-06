
class Microwave:
​
  def __init__(self, tm = '00:00'):
    
    self.mins, self.secs = [int(t) for t in tm.split(':')]
​
    while self.secs >= 60:
      self.mins += 1
      self.secs -= 60
    
    mins = str(self.mins)
    secs = str(self.secs)
​
    while len(mins) < 2:
      mins = '0' + mins
    while len(secs) < 2:
      secs = '0' + secs
    
    self.time = '{}:{}'.format(mins, secs)
​
  def __str__(self):
    return self.time
​
  def add_30(self):
    
    self.secs += 30
    while self.secs >= 60:
      self.mins += 1
      self.secs -= 60
    
    mins = str(self.mins)
    secs = str(self.secs)
    
    while len(mins) < 2:
      mins = '0' + mins
     
    while len(secs) < 2:
      secs = '0' + secs
    
    self.time = '{}:{}'.format(mins, secs)
    
    return True
  
  def input(self, inpt):
    tm = ''
    c = 0
    b_press = False
    for item in inpt:
      if item != ':':
        if b_press == False:
          if item != '0':
            b_press = True
            tm += item
            c += 1
        else:
          tm += item
          c += 1
    while len(tm) < 4:
      tm = '0' + tm
    tm = '{}:{}'.format(tm[:2], tm[2:])
    mins = int(tm[:2])
    secs = int(tm[3:])
​
    self.time = tm
    self.mins = mins
    self.secs = secs
​
    return c
​
  def __eq__(self, other):
    return self.time == other.time
​
  def __lt__(self, other):
    return (self.mins * 60 + self.secs) < (other.mins * 60 + other.secs)
​
def microwave_buttons(t):
​
  m1 = Microwave()
  m2 = Microwave()
​
  goal = Microwave(t)
​
  c1 = 0
  while m1 < goal:
    m1.add_30()
    c1 += 1
  
  if m1 == goal:
    c1valid = True
  else:
    c1valid = False
  
  c2 = m2.input(t)
​
  if c1valid == True:
    return min(c1, c2) + 1
  else:
    return c2 + 1

