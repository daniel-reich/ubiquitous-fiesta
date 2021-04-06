
class Person:
  def __init__(self,name,likely_foods,unlikely_foods):
    self.name = name
    self.likely_foods = likely_foods
    self.unlikely_foods = unlikely_foods
  def taste(self,food):
    self.food = food
    if self.food in self.likely_foods:
      return '{} eats the {} and loves it!'.format(self.name,self.food)
    elif self.food in self.unlikely_foods:
      return '{} eats the {} and hates it!'.format(self.name,self.food)
    else : return "{} eats the {}!".format(self.name,self.food)

