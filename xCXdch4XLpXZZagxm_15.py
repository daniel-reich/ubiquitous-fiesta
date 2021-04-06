
def num_of_leapyears(years):
  years_list = years.split('-')
  def leap_year(year):
    if not year % 400:
      return True
    if not year % 100:
      return False
    if not year % 4:
      return True
    else:
      return False
  return sum([leap_year(int(i)) for i in range(int(years_list[0]), int(years_list[1]) + 1)])

