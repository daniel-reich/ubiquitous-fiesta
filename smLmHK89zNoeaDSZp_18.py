
class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    # implement self.is_big
    if self.population > 250000000 or self.area > 3000000:
      self.is_big = True
    else:
      self.is_big = False
    
  def compare_pd(self, other):
      local_pd = self.population / self.area
      other_pd = other.population / other.area
      if local_pd > other_pd:
          compare = 'larger'
      elif local_pd < other_pd:
          compare = 'smaller'
      else:
          compare = 'same'
      return self.name + ' has a ' + compare + ' population density than ' + other.name

