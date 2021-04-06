
from calendar import isleap
def num_of_leapyears(years):
  first_year, last_year = years.split("-")
  return len([foo for foo in range(int(first_year), int(last_year) + 1) if isleap(foo)])

