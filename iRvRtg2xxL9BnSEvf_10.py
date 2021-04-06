
class Person:
  def __init__(self, name, love, hate):
    self.name = name
    self.love = love
    self.hate = hate
    
  def taste(self, food):
    if food in self.love:
      return "{} eats the {} and loves it!".format(self.name, food)
    elif food in self.hate:
      return "{} eats the {} and hates it!".format(self.name, food)
    else:
      return "{} eats the {}!".format(self.name, food)

