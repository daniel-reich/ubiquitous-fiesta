
class Person:
  def __init__(self, name, likes, hates):
    self.name = name
    self.likes = likes
    self.hates = hates
    
  def taste(self, food):
    opinion = ""
    if food in self.likes:
      opinion = "loves it!"
      return "{} eats the {} and {}".format(self.name, food, opinion)
    if food in self.hates:
      opinion = "hates it!"
      return "{} eats the {} and {}".format(self.name, food, opinion)
    else:
      return "{} eats the {}!".format(self.name, food)

