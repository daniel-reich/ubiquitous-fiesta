
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    self.is_big = population>250000000 or area > 3000000
    
    # implement self.is_big
    
  def compare_pd(self, other):
    p =['smaller', 'larger'] [(self.population/self.area) > (other.population / other.area)] 
    return "{} has a {} population density than {}".format(self.name, p, other.name)

