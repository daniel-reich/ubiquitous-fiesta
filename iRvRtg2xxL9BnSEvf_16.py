
class Person:
  def __init__(self, name, food_like, food_hate):
    self.name = name
    self.food_like = food_like
    self.food_hate = food_hate
  
  def taste(self, food):
    if food in self.food_like:
      return '{} eats the {} and loves it!'.format(self.name, food)
    
    elif food in self.food_hate:
      return '{} eats the {} and hates it!'.format(self.name, food)
    
    else:
      return '{} eats the {}!'.format(self.name, food)

