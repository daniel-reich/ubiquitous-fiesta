
class Country:
​
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big=False
        if self.area>3000000 or self.population>250000000:
            self.is_big=True           
​
    def pop_density(self):
        return self.population/self.area
​
    def compare_pd(self, other):
        if self.pop_density()>other.pop_density():
            return ("%s has a larger population density than %s" %(self.name, other.name))
        else:
            return ("%s has a smaller population density than %s" %(self.name, other.name))

