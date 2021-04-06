
class Person:
  def __init__(self, name, likes, hates):
    self.name = name
    self.likes = likes
    self.hates = hates
    
  def taste(self, food):
    a = ''
    if food in self.likes: a = ' and loves it'
    elif food in self.hates: a = ' and hates it'
    return '{} eats the {}{}!'.format(self.name, food, a)

