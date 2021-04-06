
class Person:
  def __init__(self,name,like,hate):
    self.name=name
    self.like=like
    self.hate=hate
  def taste(self,food):
    if food in self.like:
      return '{} eats the {} and loves it!'.format(self.name,food)
    elif food in self.hate:
      return '{} eats the {} and hates it!'.format(self.name,food)
    else:
      return '{} eats the {}!'.format(self.name,food)

