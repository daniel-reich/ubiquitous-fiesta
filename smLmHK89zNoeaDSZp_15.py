
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    # implement self.is_big
    if population > 250000000 or area > 3000000:
      self.is_big = True
    else:
      self.is_big = False
    
  def compare_pd(self, other):
    otherdensity = other.population / other.area
    selfdensity = self.population / self.area
    if otherdensity < selfdensity:
      return "{} has a larger population density than {}".format(self.name,other.name)
    else:
      return "{} has a smaller population density than {}".format(self.name,other.name)

