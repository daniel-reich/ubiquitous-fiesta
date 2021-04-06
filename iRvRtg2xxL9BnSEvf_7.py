
class Person:
  def __init__(self, name, liked_food, hated_food):
    self.name=name
    self.liked_food=liked_food
    self.hated_food=hated_food
    
  def taste(self, food):
    if food in self.liked_food:
      return '{} eats the {} and loves it!'.format(self.name,food)
    elif food in self.hated_food:
      return '{} eats the {} and hates it!'.format(self.name,food)
    else:
      return '{} eats the {}!'.format(self.name,food)

