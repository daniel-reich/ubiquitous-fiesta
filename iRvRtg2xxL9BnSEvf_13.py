
class Person:
  def __init__(self, name, like_foods, hate_foods):
    self.name = name
    self.like_foods = like_foods
    self.hate_foods = hate_foods
  def taste(self, food):
    if food in self.like_foods:
      return '{} eats the {} and loves it!'.format(self.name, food)
    elif food in self.hate_foods:
      return '{} eats the {} and hates it!'.format(self.name, food)
    else:
      return '{} eats the {}!'.format(self.name, food)

