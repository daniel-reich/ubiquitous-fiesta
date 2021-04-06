
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    self.is_big = population >= 250000000 or area >= 3000000
    
  def compare_pd(self, other):
    if self.population / self.area > other.population / other.area:
      return '{} has a larger population density than {}'.format(self.name, other.name)
    else:
      return '{} has a smaller population density than {}'.format(self.name, other.name)

