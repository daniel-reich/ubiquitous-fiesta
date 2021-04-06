
def num_of_leapyears(years):
  
  def is_leap(y):
    return y%400 == 0 or y%100 != 0 and y%4 == 0
  
  yirs = list(map(int, years.split('-')))
  
  return len([y for y in range(yirs[0], yirs[1]+1) if is_leap(y)])

