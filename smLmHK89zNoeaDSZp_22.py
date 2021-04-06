
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    self.is_big = False
    # implement self.is_big
    if (population > 250000000) or (area > 3000000):
      self.is_big = True
  def compare_pd(self, other):
    # code
    if self.population/self.area > other.population/other.area:
      return self.name + " has a larger population density than " + other.name
    return self.name + " has a smaller population density than " + other.name

