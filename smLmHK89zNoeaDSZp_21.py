
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    self.is_big = self.population > 250000000 or self.area > 3000000
    self.pd = self.population / self.area
    
    
  def compare_pd(self, other):
    res = self.pd > other.pd
    txt = "{} has a {} population density than {}"
    return txt.format(self.name, ["smaller", "larger"][res], other.name)

