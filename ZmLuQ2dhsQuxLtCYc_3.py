
class Date:
  def is_leapyear(year):
    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          return True
        return False
      return True
    return False
  
  thirty_one = [1, 3, 5, 7, 8, 10, 12]
  
  def __init__(self, date):
    self.date = date
    
    self.year, self.month, self.day = [int(obj) for obj in self.date.split(',')]
    self.ly = Date.is_leapyear(self.year)
    
    self.all_days = 0
    
    for n in range(1, self.year):
      if Date.is_leapyear(n) == True:
        self.all_days += 366
      else:
        self.all_days += 365
    
    for month in range(1, self.month):
      if month in Date.thirty_one:
        self.all_days += 31
      elif month == 2:
        if self.ly == True:
          self.all_days += 29
        else:
          self.all_days += 28
      else:
        self.all_days += 30
    
    self.all_days += self.day
  
  def days_btn(self, other):
    
    if self.all_days > other.all_days:
      return False
    else:
      return other.all_days - self.all_days
​
class Provider:
  
  def __init__(self, unit_price, standing_rate):
    self.up = unit_price
    self.sr = standing_rate
    self.tax = .05
  
  def price(self, start_meter, start_date, end_meter, end_date):
    
    units_used = end_meter - start_meter
    days_used = start_date.days_btn(end_date)
    
    if days_used == False:
      return "Invalid date"
    elif units_used < 0:
      return "Invalid meter readings"
    else:
      #print(units_used, days_used)
      unit_cost = units_used * self.up
      day_cost = days_used * self.sr
      
      total_before_tax = unit_cost + day_cost
      
      total = str(round(total_before_tax + (total_before_tax * self.tax), 2))
      
      if '.' not in total:
        total += '.00'
      
      if total[-2] == '.':
        total += '0'
      
      return '$' + total
      
def energy_bill(start_date, end_date, start_read, end_read, unit_price, standing_rate):
  
  sd = Date(start_date)
  ed = Date(end_date)
  
  meter = Provider(unit_price, standing_rate)
  
  return meter.price(start_read, sd, end_read, ed)

