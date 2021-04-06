
def interview(lst, tot):
  
  class Test:
    
    very_easy = 5
    easy = 10
    medium = 15
    hard = 20
    
    def __init__(self, questions):
      self.q = questions
    
    def check_time(self, quid, time):
      if self.q[quid] == 'VE':
        goal = Test.very_easy
      elif self.q[quid] == 'E':
        goal = Test.easy
      elif self.q[quid] == 'M':
        goal = Test.medium
      else:
        goal = Test.hard
      
      return time <= goal
    
    def check_total(self, time):
      return time <= 120
  
  if len(lst) < 8 or tot > 120:
    return 'disqualified'
  test = Test('VE,VE,E,E,M,M,H,H'.split(','))
  
  for n in range(len(lst)):
    if test.check_time(n, lst[n]) == False:
      return 'disqualified'
  
  if test.check_total(tot) == False:
    return 'disqualified'
  else:
    return 'qualified'

