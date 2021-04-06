
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    self.is_big = population>250*10**6 or area>3*10**6
    self.dens = population/area
    
  def compare_pd(self, other):
    sen = "{} has a {} population density than {}"
    return sen.format(self.name,("smaller" if self.dens<other.dens else "larger"), other.name)

