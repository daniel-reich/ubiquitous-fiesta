
class Person:
  
  def __init__(self,name, like_food, hate_food):
    self.name = name
    self.like_food = like_food
    self.hate_food = hate_food
    
  def taste(self, food):
    if food in self.like_food:
      return '{} eats the {} and loves it!'.format(self.name, food)
    if food in self.hate_food:
      return '{} eats the {} and hates it!'.format(self.name, food)
    else:
      return '{} eats the {}!'.format(self.name, food)

