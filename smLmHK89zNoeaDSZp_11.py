
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
    pop_density_other = other.population / other.area
    pop_density_self = self.population / self.area
    if pop_density_other > pop_density_self:
      return '{} has a smaller population density than {}'.format(self.name, other.name)
    else:
      return '{} has a larger population density than {}'.format(self.name, other.name)
australia = Country('Australia', 23545500, 7692024)
andorra = Country('Andorra', 76098, 468)
brazil = Country('Brazil', 202794000, 8515767)
china = Country('China', 1393000000, 9597000)
madagascar = Country('Madagascar', 26260000, 587000)

