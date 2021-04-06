
class Pay:
  
  def __init__(self, monthly, multiplier):
    self.month = monthly
    self.mult = multiplier
  
  def advance_to(self, goal):
    c = 0
    price = 0
    
    while price < goal:
      price += self.month
      self.month *= self.mult
      c += 1
    
    return c
​
def million_in_month(first_month, multiplier):
  
  employee = Pay(first_month, multiplier)
  
  return employee.advance_to(1000000)

