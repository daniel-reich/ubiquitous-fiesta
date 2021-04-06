
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    if self.population > 250000000 or self.area > 3000000:
      self.is_big = True
    else:
      self.is_big = False
    
  def compare_pd(self, other):
    density = self.population / self.area
    otherdensity = other.population / other.area
    if density > otherdensity:
      return '{} has a larger population density than {}'.format(self.name,other.name)
    else:
      return '{} has a smaller population density than {}'.format(self.name,other.name)

