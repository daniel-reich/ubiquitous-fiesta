
class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.area >= 3 * pow(10, 6)
        self.density = round(self.population / self.area)
        
    def compare_pd(self, other):
        condition = 'larger' if self.density > other.density else 'smaller'
        return '{country} has a {condition} population density than {other_country}'.format(country = self.name, condition = condition, other_country = other.name)

