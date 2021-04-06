
class Country:
  def __init__(self,name,population,area):
    self.name=name
    self.population=population
    self.area=area
    self.is_big=self.area>3*10**6or self.population>25*10**7
  def compare_pd(self,other):
    a=self.population/self.area
    b=other.population/other.area
    return'{0} has a {2} population density than {1}'.format(self.name,other.name,'larger'if a>b else'smaller')

