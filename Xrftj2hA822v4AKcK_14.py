
def leap_year(year):
  leap=True
  if ((year%400==0)or((year%4==0)and(year%100!=0))):
    leap=True
  else:
    leap=False
    
  return leap

