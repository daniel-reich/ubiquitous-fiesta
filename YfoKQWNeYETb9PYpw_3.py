
class entry:
  def __init__(self, attr):
    self.cost=attr['cost_price']
    self.sell=attr['sell_price']
    self.inventory=attr['inventory']
  
  def prof(self):
    return((self.sell-self.cost)*self.inventory)
  
def profit(info):
  return(round(entry(info).prof()))

