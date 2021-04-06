
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    # implement self.is_big
    self.density = self.population/self.area
    self.is_big = False
    if self.population > 250000000 or self.area > 3000000:
      self.is_big = True
    
  def compare_pd(self, other):
    # code
    l = ['smaller' if self.density < other.density else 'larger' for i in range(1)]
    return self.name + ' has a '+l[0]+' population density than '+other.name

