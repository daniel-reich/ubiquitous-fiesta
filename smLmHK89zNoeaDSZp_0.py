
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    self.density = self.population / self.area
    self.is_big = population > 25e7 or area > 3e6
    
  def compare_pd(self, other):
    result = ['smaller', 'larger'][self.density > other.density]
    return '{} has a {} population density than {}'.format(self.name, result, other.name)

