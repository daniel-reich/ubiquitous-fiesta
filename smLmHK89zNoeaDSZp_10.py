
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    if self.population > 250000000 or self.area >3000000:
      self.is_big = True
    else:
      self.is_big = False
    self.p_density = self.population / self.area
    
  def compare_pd(self, other):
    if self.p_density > other.p_density:
      return "{} has a larger population density than {}".format(self.name, other.name)
    elif self.p_density < other.p_density:
      return "{} has a smaller population density than {}".format(self.name, other.name)

