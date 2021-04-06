
months_per_day = [31,28,31,30,31,30,31,31,30,31,30,31]
def leap_year(y):
  if y % 4 == 0:
    if y % 100 == 0:
      return y % 400 == 0
    return True
  return False
class Date:
  def __init__(self,date):
    self.y = int(date[4::])
    self.m = int(date[2:4])
    self.d = int(date[:2])
  
  def nth_day(self):
    if self.d == 29 and self.m == 2:
      return 60
    days = sum(months_per_day[:self.m-1]) + self.d
    if leap_year(self.y) and self.m > 2:
      days += 1
    return days
def days_between_dates(d1, d2):
  date1,date2 = Date(d1),Date(d2)
  if date1.y == date2.y:
    return abs(date1.nth_day()-date2.nth_day())
  if date1.y > date2.y:
    date1,date2 = Date(d2),Date(d1)
  nth_date1 = date1.nth_day()
  nth_date2 = date2.nth_day()
  total_days = 365 * (date2.y - date1.y)
  leap_years = len(list(filter(lambda x: leap_year(x),range(date1.y,date2.y))))
  return nth_date2 + total_days + leap_years - nth_date1

