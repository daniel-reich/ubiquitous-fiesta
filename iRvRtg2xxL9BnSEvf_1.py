
class Person:
​
  def __init__(self, name, love=[], hate=[]):
    self.name = name
    self.love = love
    self.hate = hate
​
  def taste(self, food_name):
    txt = '{} eats the {}'.format(self.name, food_name)
    if food_name in self.love:
      return txt + ' and loves it!'
    elif food_name in self.hate:
      return txt + ' and hates it!'
    else:
      return txt + '!'

