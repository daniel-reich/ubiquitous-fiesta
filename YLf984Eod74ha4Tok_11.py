
def leap_year(yr):
  year=yr%100
  if year==00 and yr%400==0:
    return True
  elif year!=00 and yr%4==0:
    return True
  else: 
    return False

