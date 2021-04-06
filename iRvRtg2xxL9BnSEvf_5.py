
class Person:
​
  def __init__(self, name, likes, hates):
    self.name = name
    self.likes = likes
    self.hates = hates
  
  def taste(self, food):
    tag = ""
    if food in self.likes: tag = " and loves it"
    if food in self.hates: tag = " and hates it"
    return "{} eats the {}{}!".format(self.name, food, tag)

