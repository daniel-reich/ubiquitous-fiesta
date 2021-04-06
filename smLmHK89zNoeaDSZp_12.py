
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    # implement self.is_big
    self.is_big = self.population > 250000000 or self.area > 3000000
    
  def compare_pd(self, other):
    selfDens = self.population / self.area
    otherDens = other.population / other.area
    if selfDens > otherDens: 
      return self.name +  " has a larger population density than " + other.name
    else:
      return self.name +  " has a smaller population density than " + other.name

