
class Person:
  def __init__(self, name, fl, fh):
    self.name = name
    self.fl = fl
    self.fh = fh
  
  def taste(self, food):
    if food in self.fl:
      end = " and loves it!"
    elif food in self.fh:
      end = " and hates it!"
    else:
      end = "!"
    return self.name + " eats the " + food + end

