
class Date:
  thirty_one = [1, 3, 5, 7, 8, 10, 12]
  def is_leapyear(year):
    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          return True
        return False
      return True
    return False
    
  def __init__(self, string):
    
    self.raw = string
    
    self.day = int(string[:2])
    self.month = int(string[2:4])
    self.year = int(string[4:])
    
    self.days_since_start = 0
    
    for year in range(1, self.year):
      if Date.is_leapyear(year) == True:
        self.days_since_start += 366
      else:
        self.days_since_start += 365
    
    for month in range(1, self.month):
      if month in Date.thirty_one:
        self.days_since_start += 31
      elif month == 2:
        if Date.is_leapyear((self.year)) == True:
          self.days_since_start += 29
        else:
          self.days_since_start += 28
      else:
        self.days_since_start += 30
    
    self.days_since_start += self.day
  
  def days_between(self, other):
    return abs(self.days_since_start - other.days_since_start)
​
def days_between_dates(d1, d2):
​
  d1 = Date(d1)
  d2 = Date(d2)
  
  return d1.days_between(d2)

