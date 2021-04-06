
def leap_year(y):
  if y%4:return 0
  if y%400==0:return 1
  if y%100==0:return 0
  return 1

