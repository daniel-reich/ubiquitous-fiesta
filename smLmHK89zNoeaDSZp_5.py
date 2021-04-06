
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    
  @property
  def is_big(self):
    return True if self.population > 250000000 or self.area > 3000000 else False
    
  def compare_pd(self, other):
    first_pd = self.population/self.area
    second_pd = other.population/other.area
    s = "smaller" if first_pd < second_pd else "larger"
    return "{0} has a {1} population density than {2}".format(self.name,s,other.name)

