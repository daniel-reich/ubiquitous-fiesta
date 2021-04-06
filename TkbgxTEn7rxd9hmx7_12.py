
class Composer:
  count = 0
  def __init__(self, name, year, location):
    self.name = name
    self.year = year
    self.location = location
    Composer.count+=1

