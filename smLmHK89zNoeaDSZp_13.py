
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    # implement self.is_big
    self.is_big = population > 250*10**6 or area > 3*10**6
    
  def compare_pd(self, other):
    # code
    a, b = self.population/self.area, other.population/other.area
    comp = 'larger' if a > b else 'smaller'
    return "{} has a {} population density than {}".format(self.name, comp, other.name)

