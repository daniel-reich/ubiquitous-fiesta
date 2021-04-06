
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    self.pdens = population / area
    self.is_big = self.population > 2.5 * 10**8 or self.area > 3*10**6
    
  def compare_pd(self, other):
    report_str = '%s has a %s population density than %s'
    if self.pdens < other.pdens:
      comp_str = 'smaller'
    else:
      comp_str = 'larger'
      
    return report_str % (self.name, comp_str, other.name)

