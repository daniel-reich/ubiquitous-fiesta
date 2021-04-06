
def has_friday_13(month, year):
  import datetime
  
  
  d2=datetime.date(year,month,13)
  c=d2.isoweekday()
  if c ==5:
   return True
  else:
   return False

