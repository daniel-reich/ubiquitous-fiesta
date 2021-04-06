
def num_of_leapyears(years):
  f, l = map(int, years.split('-'))
  is_lp = lambda y: y % 400 == 0 or y % 100 != 0 and y % 4 == 0
  
  return sum(is_lp(i) for i in range(f, l+1))

