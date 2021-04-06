
class Coin_Machine:
  class User:
​
    def __init__(self, coins = 3):
      self.c = coins
      self.action = None
    
    def steal(self, other):
      if other.action == 'share':
        self.c += 3
      return True
​
    def share(self, other):
      if other.action == 'share':
        self.c += 3
      self.c -= 1
      return True
  
  def __init__(self, u1, u2):
​
    self.u1 = Coin_Machine.User(u1)
    self.u2 = Coin_Machine.User(u2)
​
  def action(self, u1action, u2action):
​
    self.u1.action = u1action
    self.u2.action = u2action
​
    if self.u1.action == 'steal':
      self.u1.steal(self.u2)
    if self.u1.action == 'share':
      self.u1.share(self.u2)
    
    if self.u2.action == 'steal':
      self.u2.steal(self.u1)
    if self.u2.action == 'share':
      self.u2.share(self.u1)
    
    return True
  
  def info(self):
    return [self.u1.c, self.u2.c] 
​
​
def get_coin_balances(lst1, lst2):
​
  cm = Coin_Machine(3, 3)
​
  for n in range(len(lst1)):
    cm.action(lst1[n], lst2[n])
  
  return cm.info()

