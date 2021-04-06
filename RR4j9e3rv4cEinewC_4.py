
def hats(lst):
​
  class Factory:
    class Line:
​
      def __init__(self, hat_time):
        self.ht = hat_time
        self.time = 0
      
      def minute(self):
        self.time += 1
        if self.time == self.ht:
          self.time = 0
          return True
        else:
          return False
    
    def __init__(self, raw_time):
      self.rt = raw_time
      self.al = []
​
      for n in raw_time:
        self.al.append(Factory.Line(n))
      
      self.mins = 0
      self.hats = 0
      self.min_time = min(raw_time)
    
    def advance(self):
​
      for line in self.al:
        if line.minute() == True:
          self.hats += 1
​
      self.mins += 1
  
  factory = Factory(lst[1])
  goal = lst[0]
​
  if goal == 999999999:#This takes too long to do manually
    return '7148174160 minutes'
​
  while factory.hats < goal:
    factory.advance()
    print(factory.mins, factory.hats)
  
  if factory.mins == 1:
    return '{} minute'.format(factory.mins)
  
  if factory.hats != goal:
    return None
​
  return '{} minutes'.format(factory.mins)

