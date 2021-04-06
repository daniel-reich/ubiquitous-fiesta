
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    # implement self.is_big
    self.is_big = self.population > 250000000 or self.area > 3000000
    
  def compare_pd(self, other):
    first_country_density = self.area / self.population
    second_country_density = other.area / other.population
    if first_country_density > second_country_density:
      return self.name + " has a smaller population density than " + other.name
    return self.name + " has a larger population density than " + other.name

